from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello (request):
    return HttpResponse("Done!")

music_list = [
    {"id":1, "name":"song1", "singer":"ghomayshi"},
    {"id":2, "name":"song2", "singer":"shadmehr"},
    {"id":3, "name":"song3", "singer":"mohsen yeganeh"}
]

def musics(request):
    data = ""
    for item in music_list:
        data = data + f"id: {item['id']} , name: {item['name']} , singer: {item['singer']}<br>"
    return HttpResponse(data)



def detail(request):
    
    return HttpResponse("music detial!")