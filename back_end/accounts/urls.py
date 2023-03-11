from django.urls import path, include
from . import views

urlpatterns = [
    path('delete/', views.user_delete),
    path('follow/<str:username>/', views.follow),
    path('<str:username>/', views.profile),
]