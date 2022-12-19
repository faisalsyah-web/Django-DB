from django.contrib import admin
from .models import Penerbangan, Bandara, Penumpang

# Register your models here.
admin.site.register(Bandara)
admin.site.register(Penerbangan)
admin.site.register(Penumpang)