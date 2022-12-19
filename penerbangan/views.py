from django.shortcuts import render
from .models import Penerbangan, Penumpang
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(
        request, "penerbangan/index.html", {"dftpenerbangan": Penerbangan.objects.all()}
    )


def penerbangan(request, penerbangan_id):
    penerbangan = Penerbangan.objects.get(pk=penerbangan_id)
    return render(
        request,
        "penerbangan/hlmninfo.html",
        {
            "penerbangan": penerbangan,
            "Penumpang": penerbangan.dftrpenumpang.all(),
            "bkn_penumpang": Penumpang.objects.exclude(
                dftrpenerbangan=penerbangan
            ).all(),
        },
    )


def pesan(request, penerbangan_id):
    if request.method == "POST":
        penerbangan = Penerbangan.objects.get(pk=penerbangan_id)
        penumpang = Penumpang.objects.get(pk=int(request.POST["penumpang"]))
        penumpang.dftrpenerbangan.add(penerbangan)
        return HttpResponseRedirect(reverse("penerbangan", args=(penerbangan.id,)))
