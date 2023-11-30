from django.shortcuts import render
from django.http import HttpResponse    
from .models import Nota
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
import datetime
from django.urls import reverse_lazy
# Create your views here.
def lista(request):
    title = Nota.objects.all()
    return render(request, 'index.html',{
        'title' : title

    })




class crearNota(CreateView):
    template_name = 'nueva.html'
    model = Nota
    fields = ['titulo','contenido','fecha']

    def get_initial(self):
     
        initial = super().get_initial()
        initial['fecha'] = datetime.date.today()  
        return initial
    
    def get_success_url(self):
        return reverse_lazy('main')
    

class UpdateNota(UpdateView):
    template_name = 'update.html'
    model = Nota
    fields=['titulo','contenido']

    def get_success_url(self):
        return reverse_lazy('main')
    


def verNotas(request, nota_id):
    nota = Nota.objects.get(id=nota_id)
    return render(request,'nota.html',{'nota':nota})


class deleteNota(DeleteView):
    template_name ='borrar.html'
    model= Nota
    
    def get_success_url(self):
        return reverse_lazy('main')
    
    
