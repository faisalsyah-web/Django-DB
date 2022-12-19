from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:penerbangan_id>", views.penerbangan, name="penerbangan"),
    path("<int:penerbangan_id>/pesan", views.pesan, name="pesan")
]
