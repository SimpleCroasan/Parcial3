from django.shortcuts import render
from django.http import HttpResponse    

# Create your views here.
def nota(request):
    return render(request, 'nota.html')


def lista(request):
    return render(request,'index.html')