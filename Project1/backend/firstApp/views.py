import os
import json
import logging
from django.http import JsonResponse, HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def store_name(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = TaskSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'success': True, 'message': 'Data stored successfully'})
            return JsonResponse({'success': False, 'message': serializer.errors}, status=400)
        except Exception as e:
            logger.exception("Error storing data: %s", str(e))
            return JsonResponse({'success': False, 'message': 'Failed to store Data'}, status=500)
    else:
        return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

@csrf_exempt
def delete_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_to_delete = data.get('id')
            if id_to_delete:
                task = Task.objects.get(id=id_to_delete)
                task.delete()
                return JsonResponse({'success': True, 'message': f'Data with ID {id_to_delete} deleted successfully'})
            else:
                return JsonResponse({'success': False, 'message': 'No ID provided'}, status=400)
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'message': f'ID {id_to_delete} not found'}, status=404)
        except Exception as e:
            logger.exception("Error deleting data: %s", str(e))
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

@csrf_exempt
def search_task_details(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            search_id = data.get('id')
            if search_id:
                task = Task.objects.get(id=search_id)
                serializer = TaskSerializer(task)
                return JsonResponse(serializer.data)
            else:
                return JsonResponse({'error': 'No ID provided'}, status=400)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)
        except Exception as e:
            logger.exception("Error in search_task_details view: %s", str(e))
            return JsonResponse({'error': 'Failed to search task details'}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_data(request):
    try:
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Exception as e:
        logger.exception("Error getting data: %s", str(e))
        return JsonResponse({'error': 'Failed to get data'}, status=500)

def download_data(request):
    try:
        file_path = "documentation.pdf"
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), as_attachment=True)
        else:
            return HttpResponse("File not found", status=404)
    except Exception as e:
        return HttpResponse(str(e), status=500)


def read_data_from_file():
    try:
        with open('name.txt', 'r') as file:
            lines = file.readlines()
            print("Lines from file:", lines) 
            data = []
            current_entry = {}
            for line in lines:
                line = line.strip() 
                if line.startswith('Id:'):
                    if current_entry: 
                        data.append(current_entry)
                    current_entry = {'id': line.split(': ')[1]}  
                elif line.startswith('Task :'):
                    current_entry['title'] = line.split(': ')[1]  
                elif line.startswith('Due-Date :'):
                    current_entry['due_date'] = line.split(': ')[1] 
            
           
            if current_entry:
                data.append(current_entry)
                
            print("Extracted data:", data)  
            return data
    except FileNotFoundError:
        return []
    except Exception as e:
        print(e)
        return []
