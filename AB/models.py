from django.db import models

class A(models.Model):
    id = models.CharField(max_length=128, primary_key=True)  
    name = models.CharField(max_length=128)
    teacher = models.CharField(max_length=128)

    def __str__(self):
        return self.name
