from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    if request.user.is_authenticated:
        context = {
            'isim': 'Berkay2'
        }
    else:
        context = {
            'isim': 'Misafir'
        }
    return render(request, 'home.html', context)
    #return HttpResponse('<b>Hoşgeldiniz</b>')