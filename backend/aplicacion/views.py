# aplicacion/views.py

from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import AplicacionSerializer      # add this
from .models import Aplicacion                     # add this

class AplicacionView(viewsets.ModelViewSet):       # add this
  serializer_class = AplicacionSerializer          # add this
  queryset = Aplicacion.objects.all()              # add this