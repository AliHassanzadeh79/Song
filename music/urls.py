from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.hello),
    path('profile/', views.profile),
    path('list/', views.music_list , name='music-list'),
    path('standard-list', views.standard_music_list , name='standard-music-list'),
    path('detail/<int:id>/', views.detail , name='music-detail'),
    path('detail2/', views.detail2 ),
]
