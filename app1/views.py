from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView, View
from .forms import Userform
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import api_example
from .serializers import  api_exampleSerializer
# Create your views here.

def index(request):
     return HttpResponse("this is my first page of app1 ")
"""
def index1(request):
    return HttpResponse("this is index 1")
function based views
def index(request):
    template =loader.get_template('app1/index.html')
    context={

    }
    return HttpResponse(template.render(context,request))
"""
#class based views
class cbt(TemplateView):
    template_name='app1/index.html'


#user authentication 
class Userformview(View):
     form_class = Userform
     template_name= 'app1/register.html'

     def get(self, request): #displays the form
           form = self.form_class(None)
           return render(request, self.template_name,{'form':form})
     def post(self,request): #enter the form value
          form = self.form_class(request.POST)
          if form.is_valid():
               user= form.save(commit=False)
               username= form.cleaned_data['username']
               password= form.cleaned_data['password']
               phone_number= form.cleaned_data['phone_number']
               print(username)
               user.set_password(password)
               user.save()
               
               user = authenticate(username = username, password = password)
               
               if user is not None:
                    if user.is_active:
                         login(request, user)

                         #request user username
                         return redirect('app1:cbt')
                         
          return render(request, self.template_name,{'form':form})

# this converts data from model to json format through serialers
class examplelist(APIView):
     def get(self, request):
          values = api_example.objects.all()
          serializer = api_exampleSerializer(values, many = True)
          return Response(serializer.data)

     
