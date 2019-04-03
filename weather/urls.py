#from django.contrib import admin
from django.urls import path
from  .import views
#from django.urls import path,include

urlpatterns = [
        path('', views.index, name = 'index'),
        path('kathmandu', views.kathmandu, name = 'kathmandu'),
        path('pokhara', views.pokhara, name = 'pokhara'),
]
