from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

class HelloAPIView(APIView):
    def get(self):
        data = {
            "hello": "this is hello"
        }
        return Response(data)