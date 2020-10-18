from django.contrib import admin
from .models import Aplicacion # add this

class AplicacionAdmin(admin.ModelAdmin):  # add this
  list_display = ('title', 'description', 'completed') # add this

# Register your models here.
admin.site.register(Aplicacion, AplicacionAdmin) # add this