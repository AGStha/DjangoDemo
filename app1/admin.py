from django.contrib import admin
from .models import Questions,Choice,Answer,api_example


# Register your models here.

#This will show all the class tables in admin panel.
admin.site.register(Questions)

admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(api_example)
