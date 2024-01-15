from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=255 , verbose_name="student Name")
    email=models.EmailField(max_length=255 , verbose_name="student Email")

def __str__(self):
    return str(self.email)


