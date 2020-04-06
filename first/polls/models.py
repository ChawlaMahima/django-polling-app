from django.db import models

# Create your models here.
class Question(models.Model):
	que_text= models.CharField(max_length=200)
	date= models.DateTimeField('date published')
	
class choice(models.Model):
	choice_text= models.CharField(max_length=200)
	votes= models.IntegerField(default=0)
	question= models.ForeignKey(Question,on_delete=models.CASCADE)   