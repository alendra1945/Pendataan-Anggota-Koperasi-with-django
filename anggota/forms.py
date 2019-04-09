from django import forms
from .models import Anggota

class CreateAnggotaForm(forms.ModelForm):
	class Meta:
		model=Anggota
		fields=('no_ba','nama_anggota','alamat','no_hp','nama_penjamin','tanggal','keterangan','status')

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		for f in self.fields.values():
			f.widget.attrs={'class':'form-control'}
		self.fields['tanggal'].widget=forms.SelectDateWidget()
		self.fields['tanggal'].widget.attrs={'class':'custom-select'}
