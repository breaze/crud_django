from rest_framework.views import APIView
from rest_framework.response import Response

from proyecto.models.Persona import Persona
import json
class PersonasView(APIView):
    def post(self, request, format=None):
        cedula = request.data["cedula"]
        nombre = request.data["nombre"]
        apellido = request.data["apellido"]
        persona1 = Persona()
        persona1.cedula = cedula
        persona1.nombre = nombre
        persona1.apellido = apellido
        persona1.save()
        res = {
            "msg": "Se creo exitosamente"
        }
        return Response(res)
    
    def get(self, request, format=None):
        personas = list(Persona.objects.all().values())
        return Response(personas)
    
    def put(self, request, format=None):
        body = json.loads(request.body)
        cedula = body['cedula']
        nombre = body['nombre']
        personas = Persona.objects.filter(cedula=cedula).update(nombre=nombre)
        res = {
            "editadas": personas
        }
        return Response(res)
    def delete(self, request, format=None):
        cedula = request.GET['cedula']
        personas = Persona.objects.filter(cedula=cedula).delete()
        return Response(personas)