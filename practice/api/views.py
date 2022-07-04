import imp
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

@api_view()
def home(request):
    """
    Home Page
    """

    # data = {}
    # data['msg'] = "Hello World"
    return Response({'message':"Hello, World"})