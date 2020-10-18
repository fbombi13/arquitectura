from rest_framework import serializers
from .models import Aplicacion

class AplicacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Aplicacion
    fields = ('id', 'title', 'description', 'completed')