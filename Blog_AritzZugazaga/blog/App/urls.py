from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('post_detail/<int:pk>/', views.post_detail, name = 'post_detail'),
]