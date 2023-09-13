from django.db import models

# Create your models here.
class Film(models.Model):
    name=models.CharField(max_length=250)
    year=models.IntegerField()
    descrptn=models.TextField()
    Image=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name