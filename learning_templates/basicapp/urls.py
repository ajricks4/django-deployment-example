from django.contrib import admin
from django.urls import path, include
from basicapp.views import other, relative

app_name='basicapp'

urlpatterns = [
    path('other/', other, name='other'),
    path('relative/', relative, name='relative')
]