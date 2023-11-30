from django.shortcuts import render
from django.http import HttpResponse    
from .models import Nota
# Create your views here.
def nota(request,id):
    title = Nota.objects.get(id==id).titulo
    return render(request, 'nota.html',{
        'title' : title

    })


def lista(request):
    return render(request,'index.html')