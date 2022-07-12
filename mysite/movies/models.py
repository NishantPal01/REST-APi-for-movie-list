from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.


class MovieData(models.Model):
    def __str__(self):
        return self.movie_name

    movie_name = models.CharField(max_length=200)
    movie_time = models.FloatField()
    movie_rating = models.FloatField()
    typ = models.CharField(max_length=200,default='Action')
    image = models.ImageField(upload_to='Images/',default='Images/None/noimg.jpg')
