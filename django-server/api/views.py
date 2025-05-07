from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloWorldView(APIView) :
    # get method to handle GET requests
    def get(self, request) :
        context = {
            'message' : "Hello, World!"
        }
        return Response(context)
    
