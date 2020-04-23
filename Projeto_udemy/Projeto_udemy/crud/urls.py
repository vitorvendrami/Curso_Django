from django.urls import path
from .views import *

urlpatterns = [
	path('', listagem),
	path('listagem/', listagem),
	path('crud/listagem/', listagem),
	path('crud/listagem/<int:id>/', selecao),
	path('crud/consulta/', consulta),
	path('crud/ordenacao/<str:campo>/', ordenacao),
	path('crud/insercao/', insercao),
	path('crud/salvar_insercao/', salvar_insercao),
	path('crud/edicao/<int:id>/', edicao),
	path('crud/salvar_edicao/', salvar_edicao),
	path('crud/delecao/<int:id>/', delecao),
	path('crud/salvar_delecao/', salvar_delecao),
	path('crud/graficos/', graficos)
]
