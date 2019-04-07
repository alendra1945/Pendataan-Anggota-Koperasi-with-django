from django.urls import path
from .views import ListPenagihanView,CreatePenagihanView,DeletePenagihanView,SearchView




app_name='penagihan'

urlpatterns=[
	path('export/',ListPenagihanView.as_view(mode='export'),name='export'),
	path('search/',SearchView.as_view(),name='search'),
	path('search/export/',SearchView.as_view(mode='export'),name='search_exp'),
	path('tambahdata/',CreatePenagihanView.as_view(mode=''),name='tambahdata'),
	path('ubah/<int:id_penagihan>/',CreatePenagihanView.as_view(mode='ubah'),name='ubah'),
	path('hapus/<int:id_penagihan>/',DeletePenagihanView.as_view(),name='hapus'),
	path('',ListPenagihanView.as_view(),name='home'),
]