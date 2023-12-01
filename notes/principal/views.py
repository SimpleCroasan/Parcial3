from django.shortcuts import render
from django.http import HttpResponse    
from .models import Nota
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
import datetime
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.template import loader
from django.shortcuts import redirect
from .forms import NewUserForm

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
    
    
def registro(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Registro Exitoso")
            return redirect('main')
        messages.error(request,"No fue posible el Registro. Información Invalida")
    form = NewUserForm()
    context = {"register_form":form}
    template = loader.get_template("register.html") 
    return HttpResponse(template.render(context,request))