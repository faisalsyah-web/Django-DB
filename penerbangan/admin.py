from django.contrib import admin
from .models import Penerbangan, Bandara, Penumpang

# Register your models here.
class PenerbanganAdmin(admin.ModelAdmin):
    list_display = ("id", "asal", "tujuan", "durasi")

class PenumpangAdmin(admin.ModelAdmin):
    filter_horizontal = ("dftrpenerbangan", )

admin.site.register(Bandara)
admin.site.register(Penerbangan, PenerbanganAdmin)
admin.site.register(Penumpang, PenumpangAdmin)