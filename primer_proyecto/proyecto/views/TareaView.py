from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date
from proyecto.models.Persona import Persona
from proyecto.models.Tarea import Tarea
import json
class TareaView(APIView):
    def post(self, request, format=None):
        nombre = request.data['nombre']
        descripcion = request.data['descripcion']
        #fecha_creacion = date.strptime(request.data['fecha_creacion'], '%d/%m/%y')
        fecha_creacion = request.data['fecha_creacion']
        responsable = Persona()
        responsable.cedula = request.data['responsable']
        tarea = Tarea()
        tarea.nombre = nombre
        tarea.descripcion = descripcion
        tarea.fecha_creacion = fecha_creacion
        tarea.responsable = responsable
        tarea.save()
        res = {
            "msg": "Creado Exitosamente"
        }
        return Response(res)


    def get(self, request, format=None):
        tareas = Tarea.objects.all()
        responsable_id = request.GET['responsable_id']
        tareas = list(tareas.filter(responsable_id=responsable_id).values())
        return Response(tareas)

    def delete(self, request, format=None):
        id = request.GET['id']
        tareas = Tarea.objects.filter(id=id).delete()
        return Response(tareas)
    
    def put(self, request, format=None):
        body = json.loads(request.body)
        id = body['id']
        nombre = body['nombre']
        descripcion = body['descripcion']
        tareas = Tarea.objects.filter(id=id).update(nombre=nombre, descripcion=descripcion)
        res = {
            "editadas": tareas
        }
        return Response(res)