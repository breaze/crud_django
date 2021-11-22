from django.urls import path
from django.urls import path
from proyecto.views.HelloWorld import HelloWorld
from proyecto.views.PersonasView import PersonasView
from proyecto.views.TareaView import TareaView

urlpatterns = [
    path('hola_mundo/', HelloWorld.as_view()),
    path('persona/', PersonasView.as_view()),
    path('tarea/', TareaView.as_view())
]