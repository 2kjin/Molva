from rest_framework import serializers
from .models import Movie, Genre, Actor, Director, Review, Watch_Provider, MovieLike

class GenrenameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name',)

class ActornameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name','profile_path')

class DirectornameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ('name',)

class OttpathSerializer(serializers.ModelSerializer):

    class Meta:
        model = Watch_Provider
        fields = ('ott_path',)

class MovieListSerializer(serializers.ModelSerializer):
    genres = GenrenameSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_users', 'actors')

class MovieTitleSerializer(serializers.ModelSerializer):
    genres = GenrenameSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'poster_path', 'genres', 'watched_users')

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    movie = MovieTitleSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user')

class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActornameSerializer(many=True, read_only=True)
    genres = GenrenameSerializer(many=True, read_only=True)
    directors = DirectornameSerializer(many=True, read_only=True)
    ott_paths = OttpathSerializer(many=True, read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)
    
    # print(actors)
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_users','reviews')

class MovieLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieLike
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

# class ActorSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Actor
#         fields = '__all__'

# class DirectorSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Director
#         fields = '__all__'