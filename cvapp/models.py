from django.db import models

# Create your models here.
class Feedback(models.Model):
    name=models.CharField(max_length=100,blank=True)
    email=models.CharField(max_length=100)
    message=models.TextField()
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
