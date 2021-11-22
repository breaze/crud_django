from rest_framework.views import APIView
from rest_framework.response import Response

from proyecto.models.Persona import Persona

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