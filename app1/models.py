from django.db import models

# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    question_number=models.IntegerField(default=0)
    #pub_date = models.DateTimeField('date published')
class Choice(models.Model):
    choice_text=models.CharField(max_length=200)
    votes= models.IntegerField(default=0)

class Answer(models.Model):
    answer_options = models.ForeignKey(Questions,on_delete=models.CASCADE)
#api eg. 
class api_example(models.Model):
    first_field= models.CharField(max_length=10)
    second_field=models.FloatField()
    def __str__(self):
        return self.first_field
        