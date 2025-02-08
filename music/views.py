from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def hello (request):
    url = reverse('music-list')
    return HttpResponseRedirect(url)

music_list = [
    {"id":1, "name":"song1", "singer":"ghomayshi"},
    {"id":2, "name":"song2", "singer":"shadmehr"},
    {"id":3, "name":"song3", "singer":"mohsen yeganeh"}
]

def musics(request):
    # data = ""
    # for item in music_list:
    #     data = data + f"{item['id']} : <a href='http://127.0.0.1:8000/music/detail/{item['id']}' target='_blank'>{item['name']}</a><br>"
    # return HttpResponse(data)
    data = ""
    for item in music_list:
        url = reverse('music-detail' , args=[item["id"]])
        data = data + f"{item['id']} : <a href='{url}' target='_blank'>{item['name']}</a><br>"
    return HttpResponse(data)



def detail(request, id):
    return HttpResponse(f"id: {music_list[id-1]['id']} , name: {music_list[id-1]['name']} , singer: {music_list[id-1]['singer']}")