from django import forms
from .models import Penagihan

class CreatePenagihanForm(forms.ModelForm):
	class Meta:
		model=Penagihan
		fields=('no_ba','nama_anggota','alamat','no_hp','tanggal','keterangan')

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		for f in self.fields.values():
			f.widget.attrs={'class':'form-control'}
		self.fields['tanggal'].widget=forms.SelectDateWidget()
		self.fields['tanggal'].widget.attrs={'class':'custom-select col'}
