from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(null=True, blank=True)
    director = models.ForeignKey(Director, null=True, on_delete=models.CASCADE, related_name='movies')
   
    def __str__(self):
        return self.title

