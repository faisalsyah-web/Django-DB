from django.db import models

# Create your models here.
class Bandara(models.Model):
    kode = models.CharField(max_length=3)
    kota = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.kota} ({self.kode})"


class Penerbangan(models.Model):
    asal = models.ForeignKey(
        Bandara, on_delete=models.CASCADE, related_name="departemen"
    )
    tujuan = models.ForeignKey(
        Bandara, on_delete=models.CASCADE, related_name="kedatangan"
    )
    durasi = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.asal} to {self.tujuan}"
