from django.contrib import admin
from .models import Penerbangan, Bandara

# Register your models here.
admin.site.register(Bandara)
admin.site.register(Penerbangan)