from django.urls import path
from .views import ListAnggotaView,CreateAnggotaView,DeleteAnggotaView,SearchView




app_name='anggota'

urlpatterns=[
	path('export/',ListAnggotaView.as_view(mode='export'),name='export'),
	path('search/<str:status>/',SearchView.as_view(),name='search'),
	path('search/export/<status>/',SearchView.as_view(mode='export'),name='search_exp'),
	path('tambahdata/',CreateAnggotaView.as_view(mode=''),name='tambahdata'),
	path('ubah/<int:id_anggota>/',CreateAnggotaView.as_view(mode='ubah'),name='ubah'),
	path('hapus/<int:id_anggota>/',DeleteAnggotaView.as_view(),name='hapus'),
	path('',ListAnggotaView.as_view(),name='home'),
]