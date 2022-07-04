from django.urls import path

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('tracks', views.AlbumDetailViewSet, basename='tracks')

urlpatterns = [
    path('home/', views.home),

]

urlpatterns += router.urls