from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('get_data/', views.create_json ),
    path('', views.movie_list),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/like', views.like),
    path('<int:movie_id>/reviews/', views.review_create),
    path('reviews/<int:review_pk>', views.review_detail),
]

# python manage.py loaddata actors.json directors.json genres.json movies.json