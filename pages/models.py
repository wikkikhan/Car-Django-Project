from django.db import models

class Team(models.Model):
    firstName = models.CharField(max_length= 255)
    LastName = models.CharField(max_length=255)
    Designation = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook = models.URLField(max_length=100)
    google = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName