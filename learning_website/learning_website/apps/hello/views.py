from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from learning_website.utils.return_status import ReturnFunc
# from .serializers import HelloSerializer


# Create your views here.
class Hello(APIView):
    """
    测试方法类
    HelloWorld
    """
    def get(self, request):
        # serializer = HelloSerializer
        data = ReturnFunc().visit_success()
        return Response(data=data)
