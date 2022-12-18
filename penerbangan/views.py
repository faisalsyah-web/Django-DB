from django.shortcuts import render
from .models import Penerbangan

# Create your views here.
def index(request):
    return render(
        request, "penerbangan/index.html", {"dftpenerbangan": Penerbangan.objects.all()}
    )

def penerbangan(request, penerbangan_id):
    penerbangan = Penerbangan.objects.get(pk=penerbangan_id)
    return render(request, "penerbangan/hlmninfo.html", {
        "penerbangan": penerbangan
    })