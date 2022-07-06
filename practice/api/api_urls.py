from django.urls import path

from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r'track', views.AlbumDetailViewSet, basename='track')
track_list = views.AlbumDetailViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('home/', views.home),
    path('track/', track_list, name='track-list')

]

# urlpatterns += router.urls