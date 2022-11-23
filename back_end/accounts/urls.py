from django.urls import path, include
from . import views

urlpatterns = [
    # path('profile/', include('accounts.urls')),
    # path('delete/', views.user_delete),
    path('<str:username>/', views.profile),
]