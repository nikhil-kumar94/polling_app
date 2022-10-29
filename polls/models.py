from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    question=models.CharField(max_length=200)
    

    def __str__(self):
        return self.question


class Choices(models.Model):
    choice_name=models.CharField(max_length=200)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    replier=models.ManyToManyField(User,blank=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_name
