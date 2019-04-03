from rest_framework import serializers
from .models import api_example


class api_exampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_example
        # fields =('first_field','second_field')
        fields ='__all__' #it selects all fields 