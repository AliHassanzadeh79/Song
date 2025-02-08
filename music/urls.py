from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.hello),
    path('list/', views.musics , name='music-list'),
    path('detail/<int:id>/', views.detail , name='music-detail'),
]
