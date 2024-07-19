from django.db import models

# Create your models here.

#FlanPage
class FlanPage(models.Model):
    name = models.CharField(max_length=50)
    images = models.URLField()

    def __str__(self):
        return self.name

#Flan
class Flan(models.Model):
    name = models.CharField(max_length=50)
    flanImg = models.URLField()

    def __str__(self):
        return self.name

#FornContact
class FormContact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name

