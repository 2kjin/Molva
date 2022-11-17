from django.urls import path, include
from . import views
urlpatterns = [
    path('get_data/', views.create_json ),
    path('movie/', views.movie ),
    path('genre/', views.genre ),
    path('actor/', views.actor ),
    path('director/', views.director ),
]
