from django.shortcuts import render
from django.http import JsonResponse
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
            name = data.get('name')
            mobile = data.get('mobile')
            email = data.get('email')
            if name:
                with open('name.txt', 'a')as f:
                    f.write('Name: ' + name + "" +'Mobile Number : '+ mobile + "" + 'Email ID: ' + email )
                return JsonResponse({'success': True, 'message': 'Name stored successfully'})
            else:
                return JsonResponse({'success': False, 'message': 'No name provided'}, status=400)
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'message': 'Failed to store name'}, status=500)
    else:
        return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)
