from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add/', views.create_post_view, name='create_post'),
]