
import os
import json
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def store_name(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = data.get('id')
            title = data.get('title')
            due_date = data.get('due_date')
            if id:
                with open('name.txt', 'a') as f:
                    f.write(f'\nId: {id}\nTask : {title}\nDue-Date : {due_date}')
                return JsonResponse({'success': True, 'message': 'Data stored successfully'})
            else:
                return JsonResponse({'success': False, 'message': 'No Data provided'}, status=400)
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'message': 'Failed to store Data'}, status=500)
    else:
        return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)


def get_data(request):
    try:
        with open('name.txt', 'r') as file:
            data = file.read()
        return HttpResponse(data, content_type='text/plain')
    except FileNotFoundError:
        return HttpResponse("File not found", status=404)
    except Exception as e:
        return HttpResponse(str(e), status=500)


def download_data(request):
    try:
        file_path = "documentation.pdf"
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), as_attachment=True)
        else:
            return HttpResponse("File not found", status=404)
    except Exception as e:
        return HttpResponse(str(e), status=500)


@csrf_exempt
def delete_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_to_delete = data.get('id')
            if id_to_delete:
                with open('name.txt', 'r') as file:
                    lines = file.readlines()
                with open('name.txt', 'w') as file:
                    deleted = False
                    i = 0
                    while i < len(lines):
                        if f'Id: {id_to_delete}' in lines[i]:
                            deleted = True
                            i += 3  
                            continue
                        file.write(lines[i])
                        i += 1
                    if not deleted:
                        return JsonResponse({'success': False, 'message': f'ID {id_to_delete} not found'}, status=404)
                return JsonResponse({'success': True, 'message': f'Data with ID {id_to_delete} deleted successfully'})
            else:
                return JsonResponse({'success': False, 'message': 'No ID provided'}, status=400)
        except FileNotFoundError:
            return HttpResponseNotFound("File not found")
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    else:
        return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)
