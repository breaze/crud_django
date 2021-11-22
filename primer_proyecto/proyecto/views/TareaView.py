from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date
from proyecto.models.Persona import Persona
from proyecto.models.Tarea import Tarea

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