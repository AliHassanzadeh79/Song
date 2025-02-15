from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
# Create your views here.

musics = [
    {"id": 1, "name": "Havaye Khodaa", "singer": "Ebi"},
    {"id": 2, "name": "Zendegi", "singer": "Farhad"},
    {"id": 3, "name": "Khodahafezi", "singer": "Moein"},
    {"id": 4, "name": "Kooh", "singer": "Shadmehr Aghili"},
    {"id": 5, "name": "Har Shab", "singer": "Siavash Ghomayshi"},
    {"id": 6, "name": "Behet Ghol Midam", "singer": "Mohsen Yeganeh"},
    {"id": 7, "name": "To Ke Nisti", "singer": "Googoosh"},
    {"id": 8, "name": "Delam Tang Shodeh", "singer": "Sirvan Khosravi"},
    {"id": 9, "name": "Vay Vay", "singer": "Reza Sadeghi"}
]

def hello (request):
    url = reverse('music-list')
    return HttpResponseRedirect(url)

def profile(request):
    return render(request,"music/profile.html")


def music_list(request):
    # data = ""
    # for item in musics:
    #     data = data + f"{item['id']} : <a href='http://127.0.0.1:8000/music/detail/{item['id']}' target='_blank'>{item['name']}</a><br>"
    # return HttpResponse(data)
    data = ""
    for item in musics:
        url = reverse('music-detail' , args=[item["id"]])
        data = data + f"{item['id']} : <a href='{url}' target='_blank'>{item['name']}</a><br>"
    return HttpResponse(data)

def standard_music_list(request):
    filter_by_name = []
    name = request.GET.get('name','')
    if name == '' :
        filter_by_name.extend(musics)
    else:
        for music in musics :
            if name.lower() in music['name'].lower():
                filter_by_name.append(music)
    data = {"musics" : filter_by_name}
    return render(request,'music/list.html',context=data)

def detail(request, id):
    return HttpResponse(f"id: {musics[id-1]['id']} , name: {musics[id-1]['name']} , singer: {musics[id-1]['singer']}")

def detail2(request):
    id = int(request.GET.get('id' , 0))
    return HttpResponse(f"id: {musics[id-1]['id']} , name: {musics[id-1]['name']} , singer: {musics[id-1]['singer']}")
