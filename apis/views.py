from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins
from .serializers import ProjectsSerializer
from projects import models
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
# Create your views here.
class ListPostViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,mixins.DestroyModelMixin ):
    serializer_class=ProjectsSerializer
    queryset=models.Post.objects.all()
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    permission_classes=[IsAuthenticated]  