from django.db import models

# Create your models here.
class Students(models.Model):
    id = models.AutoField(primary_key=True)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    name=models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    objects = models.Manager()
    
class ids(models.Model):
    id_1=models.CharField(max_length=100)
    objects=models.Manager()
