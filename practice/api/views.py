from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Album
from .serializers import AlbumSerializer

from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
# Create your views here.

@api_view()
def home(request):
    """
     Home Page
    """

    data = {}
    data['msg'] = "Hello World"
    return Response({'message':"Hello, World"})

# @api_view(['GET'])
# def album_detail(request, *args, **kwargs):
#     """
#     Album detail API
#     """
#     album = Album.objects.filter()

class AlbumDetailViewSet(viewsets.ModelViewSet):
     queryset = Album.objects.all() 
     serializer_class = AlbumSerializer
     lookup_field = 'album_name'
    #  def retrieve(self, request, **kwargs):
    #     factory = APIRequestFactory()
    #     request = factory.get('/')


    #     serializer_context = {'request': Request(request)}
    #     queryset = Album.objects.all() 
    #     tracks = get_object_or_404(queryset, kwargs['album_name'])
    #     serializer = AlbumSerializer(tracks, context=serializer_context)
    #     return Response(serializer.data)