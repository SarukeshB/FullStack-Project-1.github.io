#                                                                      SARUKESH BOOMINATHAN
"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py

from django.contrib import admin
from django.urls import path
from firstApp.views import index, store_name, get_data, download_data, delete_data

urlpatterns = [
    path('', index),
    path('store-name/', store_name, name='store_name'),
    path('get-data/', get_data, name='get_data'),
    path('download/', download_data, name='download_data'),
    path('delete-data/', delete_data, name='delete_data'),
    path('admin/', admin.site.urls),
]
