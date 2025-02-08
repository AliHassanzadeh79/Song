from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.hello),
    path('list/', views.musics),
    path('detail/<int:id>/', views.detail),
]
