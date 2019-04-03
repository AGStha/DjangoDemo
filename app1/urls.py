#from django.contrib import admin
from django.urls import path
from  .import views
from django.views.generic import TemplateView
#from django.urls import path,include

urlpatterns = [
        #path('football', views.index, name = 'index'),
       # path('cricket', views.index1, name = 'index1'),
       path('', views.index, name='index'),
        #path('cbt/', views.cbt.as_view()),
        path('cbt/', TemplateView.as_view(template_name='app1/index.html') , name='cbt'),
        path('register/',views.Userformview.as_view(), name='register'),

]
