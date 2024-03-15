from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import FileResponse
import os
from django.views.decorators.csrf import csrf_exempt
import json


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
                with open('name.txt', 'a')as f:
                    f.write( '\nId: ' + id +'\nTask : '+ title +'\nDue-Date : ' + due_date)
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