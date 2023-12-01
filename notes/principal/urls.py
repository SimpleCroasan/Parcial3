from django.urls import path
from . import views
from principal.views import crearNota,UpdateView

urlpatterns=[
    path('',views.lista,name='main'),
    path('nuevo/',crearNota.as_view(),name="view" ),
    path('editar/<int:pk>',views.UpdateNota.as_view(),name="editar" ),
    path('nota/<int:nota_id>/', views.verNotas, name='nota'),
    path('borrar/<int:pk>',views.deleteNota.as_view(),name="borrar" ),
    path('registro',views.registro,name='registro')
    
]