from django.urls import path
from . import views
urlpatterns=[
    path('',views.lista),
    path('nota/',views.nota)

]