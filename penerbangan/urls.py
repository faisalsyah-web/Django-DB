from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
  path("<int:penerbangan_id>", views.penerbangan, name="Penerbangan")
]
