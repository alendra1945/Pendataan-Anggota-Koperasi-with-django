from django.db import models
import datetime
# Create your models here.

class Penagihan(models.Model):
	no_ba=models.CharField(max_length=255)
	nama_anggota=models.CharField(max_length=255)
	alamat=models.TextField()
	no_hp=models.CharField(max_length=13)
	tanggal=models.DateField(default=datetime.date.today)
	keterangan=models.TextField()

	def __str__(self):
		return self.nama_anggotas