from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('genre/', views.genre_menu),
    path('get_data/', views.create_json),
    path('<int:movie_pk>/getmovielike/', views.get_likes),
    path('<int:movie_pk>/postmovielike/', views.likes),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/reviews/', views.review_list),
    path('<int:movie_id>/reviews/', views.review_create),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('create_genre_list/<int:genre_pk>/', views.genre_list),
    path('create_ott_list/<int:ott_pk>/', views.create_ott_list),

]

#BE

# python -m venv venv
# source venv/Scripts/activate
# pip install -r requirments.txt
# python manage.py migrate
# python manage.py loaddata actors.json directors.json genres.json movies.json otts.json
# python manage.py runserver

#FE 

# npm i
# npm run serve


# python -Xutf8 manage.py dumpdata --indent 4 movies.Movie > movies.json
# python -Xutf8 manage.py dumpdata --indent 4 movies.Genre > genres.json
# python -Xutf8 manage.py dumpdata --indent 4 movies.Actor > actors.json
# python -Xutf8 manage.py dumpdata --indent 4 movies.Director > directors.json
# python -Xutf8 manage.py dumpdata --indent 4 movies.Watch_Provider > otts.json