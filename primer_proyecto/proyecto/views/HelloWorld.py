from rest_framework.views import APIView
from rest_framework.response import Response
class HelloWorld(APIView):
    def get(self, request, format="None"):
        res = {
            "msg": "Hola Mundo"
        }
        return Response(res)