from django.contrib.auth.forms import AuthenticationForm
class AccountLoginForm(AuthenticationForm):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['username'].widget.attrs={'class':'form-control','placeholder':'Masukan Username'}
		self.fields['password'].widget.attrs={'class':'form-control','placeholder':'Masukan Password'}