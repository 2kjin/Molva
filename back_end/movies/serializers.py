from rest_framework import serializers
from .models import Movie, Genre, Actor, Director

class Genrename(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name',)

class Actorname(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)

class Directorname(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ('name',)

class MovieSerializer(serializers.ModelSerializer):
    actors = Actorname(many=True, read_only=True)
    genres = Genrename(many=True, read_only=True)
    directors = Directorname(many=True, read_only=True)
    print(actors)
    class Meta:
        model = Movie
        fields = '__all__'

# class GenreSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Genre
#         fields = '__all__'

# class ActorSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Actor
#         fields = '__all__'

# class DirectorSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Director
#         fields = '__all__'
