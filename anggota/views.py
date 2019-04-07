import time
import csv
from django.db.models import Q
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import View,ListView,RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Anggota
from .forms import CreateAnggotaForm

# Create your views here.

class ExportData:
	def export_data_csv(self,Data):
		response=HttpResponse(content_type='text/csv')
		response['Content-Disposition']=f"attachment; filename=data-{time.strftime('%y%m%d%H%M%S')}"
		Data=Data.values_list('no_ba','nama_anggota','alamat','no_hp','nama_penjamin','tanggal','keterangan')
		writer=csv.writer(response)
		writer.writerow(['No BA','Nama Anggota','Alamat','No Hp','Nama Penjamin','Tanggal','Keterangan'])
		for d in Data:
			writer.writerow(d)
		return response

class ListAnggotaView(LoginRequiredMixin,ListView,ExportData):
	model=Anggota
	mode=None
	template_name='list_anggota.html'
	context_object_name='anggota'
	tahun_sekarang=int(time.strftime('%Y'))+1
	extra_context={
		'title':'Survey/TambahAnggota',
		'daf_tanggal':range(1,32),
		'daf_bulan':range(1,13),
		'daf_tahun':range(2016,tahun_sekarang)
	}

	def get_context_data(self,*args,**kwargs):
		context=super().get_context_data(*args,**kwargs)
		status=0
		context['status']=0
		if 'jenis' in self.request.GET and self.request.GET['jenis']== 'anggotabaru':
			status=1
			context['status']=1
		context['anggota']=self.model.objects.filter(status=status)
		if 'tahun' in self.request.GET and self.request.GET['tahun']!= 'all':
			tahun=self.request.GET['tahun']
			context['anggota']=self.model.objects.filter(status=status,tanggal__year=tahun)
			if 'bulan' in self.request.GET and self.request.GET['bulan']!= 'all':
				bulan=self.request.GET['bulan']
				context['anggota']=self.model.objects.filter(status=status,tanggal__year=tahun,tanggal__month=bulan)
				if 'tanggal' in self.request.GET and self.request.GET['tanggal']!= 'all':
					tanggal=self.request.GET['tanggal']
					context['anggota']=self.model.objects.filter(status=status,tanggal__year=tahun,tanggal__month=bulan,tanggal__day=tanggal)
		if self.mode=='export':
			context['data']=self.export_data_csv(context['anggota'])
		return context
	def get(self,request,*args,**kwargs):
		response=super().get(request,*args,**kwargs)
		context=self.get_context_data()
		if self.mode=='export':
			return context['data']
		return response
		
class CreateAnggotaView(LoginRequiredMixin,View):
	template_name='tambah_anggota.html'
	anggota_form=CreateAnggotaForm()
	mode=None
	context={}
	def get(self,*args,**kwargs):
		if self.mode=='ubah':
			update_data=Anggota.objects.get(id=kwargs['id_anggota'])
			data=update_data.__dict__
			self.anggota_form=CreateAnggotaForm(initial= data,instance=update_data)
			self.context['title']='Ubah Data'
		else:
			self.context['title']='Tambah data'
		self.context['forms']=self.anggota_form
		return render(self.request,self.template_name,self.context)	

	def post(self,*args,**kwargs):

		if kwargs.__contains__('id_anggota'):
			update_data=Anggota.objects.get(id=kwargs['id_anggota'])
			self.anggota_form=CreateAnggotaForm(self.request.POST,instance=update_data)
		else:
			  self.anggota_form=CreateAnggotaForm(self.request.POST)

		if self.anggota_form.is_valid():
			self.anggota_form.save()
		return redirect('anggota:home')

class DeleteAnggotaView(LoginRequiredMixin,RedirectView):
	pattern_name='anggota:home'
	permanent=False
	query_string=False
	def get_redirect_url(self,*args,**kwargs):
		delete_akun=Anggota.objects.get(id=kwargs['id_anggota'])
		delete_akun.delete()
		return super().get_redirect_url()


class SearchView(LoginRequiredMixin,ListView,ExportData):
	model=Anggota
	mode=None
	template_name='list_anggota.html'
	context_object_name='anggota'
	tahun_sekarang=int(time.strftime('%Y'))+1
	extra_context={
		'title':'Survey/TambahAnggota',
		'daf_tanggal':range(1,32),
		'daf_bulan':range(1,13),
		'daf_tahun':range(2016,tahun_sekarang)
	}

	def get_context_data(self,*args,**kwargs):
		context=super().get_context_data(*args,**kwargs)
		status=0
		context['status']=0
		if self.kwargs.__contains__('status') and self.kwargs['status']== 'anggotabaru':
			status=1
			context['status']=1
		context['anggota']=self.model.objects.filter(status=status)
		if 's' in self.request.GET and self.request.GET['s'].strip():
			search=self.request.GET['s']
			context['anggota']=self.model.objects.filter(Q(no_ba__icontains=search) | Q(nama_anggota__icontains=search) | Q(alamat__icontains=search) |  Q(nama_penjamin__icontains=search),status=status)
		context['search_export']=1
		if self.mode=='export':
			context['data']=self.export_data_csv(context['anggota'])
		return context
	def get(self,request,*args,**kwargs):
		response=super().get(request,*args,**kwargs)
		context=self.get_context_data()
		if self.mode=='export':
			return context['data']
		return response



