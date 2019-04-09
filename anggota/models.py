from django.db import models
import datetime
# Create your models here.
status_choice=(
		(0,'Survey'),
		(1,'Anggota Baru'),
	)
class Anggota(models.Model):
	no_ba=models.CharField(max_length=255)
	nama_anggota=models.CharField(max_length=255)
	alamat=models.TextField()
	no_hp=models.CharField(max_length=13)
	nama_penjamin=models.CharField(max_length=255)
	tanggal=models.DateField(default=datetime.date.today)
	keterangan=models.TextField()
	status=models.IntegerField(choices=status_choice)

	def __str__(self):
		return self.nama_anggota