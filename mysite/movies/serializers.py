from .models import MovieData
from rest_framework import serializers

class MovieSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = MovieData
        fields = ['id','movie_name','movie_time','movie_rating','typ','image']