from django.shortcuts import render
from .models import Pessoa
from django.views.decorators.csrf import csrf_protect

def listagem(request):
	titulo = 'Listagem de Pessoas'
	pessoas = Pessoa.objects.all()
	return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})

def selecao(request, id):
	titulo = 'Listagem de Pessoas'
	pessoa = Pessoa.objects.get(id=id)
	return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': [pessoa]})

@csrf_protect
def consulta(request):
	consulta = request.POST.get('consulta')
	campo = request.POST.get('campo')

	if campo   == 'nome':
		pessoas = Pessoa.objects.filter(nome__contains=consulta)
	elif campo == 'idade':
		pessoas = Pessoa.objects.filter(idade__contains=consulta)
	elif campo == 'sexo':
		pessoas = Pessoa.objects.filter(sexo__contains=consulta)
	elif campo == 'salario':
		if consulta.find(',') > 0 or consulta.find('.') > 0:
			consulta = float(consulta.replace(',', '.'))
		pessoas = Pessoa.objects.filter(salario__contains=consulta)

	titulo = 'Listagem de Pessoas'
	return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})

_campo = ''
def ordenacao(request, campo):
	titulo = 'Listagem de Pessoas'
	global _campo
	if campo == _campo:
		pessoas = Pessoa.objects.all().order_by(campo).reverse()
		_campo = ''
	else:
		pessoas = Pessoa.objects.all().order_by(campo)
		_campo = campo
	return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})

def insercao(request):
	titulo = 'Inserção de Pessoa'
	return render(request, 'insercao.html', {'titulo': titulo})

@csrf_protect
def salvar_insercao(request):
	nome = request.POST.get('nome')
	idade = request.POST.get('idade')
	sexo = request.POST.get('sexo')
	salario = request.POST.get('salario')
	salario = salario.replace(',', '.')

	objeto = Pessoa(
		nome=nome,
		idade=idade,
		sexo=sexo,
		salario=salario
	)
	objeto.save()

	titulo = 'Listagem de Pessoas'
	pessoas = Pessoa.objects.all()
	return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})

def edicao(request, id):
	titulo = 'Edição de Pessoa'
	pessoa = Pessoa.objects.get(id=id)
	return render(request, 'edicao.html', {'titulo': titulo, 'pessoa': pessoa})

@csrf_protect
def salvar_edicao(request):
	id = request.POST.get('id')
	nome = request.POST.get('nome')
	idade = request.POST.get('idade')
	sexo = request.POST.get('sexo')
	salario = request.POST.get('salario')
	salario = salario.replace(',', '.')

	Pessoa.objects.filter(id=id).update(
		nome=nome,
		idade=idade,
		sexo=sexo,
		salario=salario
	)

	titulo = 'Listagem de Pessoas'
	pessoas = Pessoa.objects.all()
	return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})

def delecao(request, id):
	titulo = 'Deleção de Pessoa'
	pessoa = Pessoa.objects.get(id=id)
	return render(request, 'delecao.html', {'titulo': titulo, 'pessoa': pessoa})

@csrf_protect
def salvar_delecao(request):
	id = request.POST.get('id')

	Pessoa.objects.filter(id=id).delete()

	titulo = 'Listagem de Pessoas'
	pessoas = Pessoa.objects.all()
	return render(request, 'listagem.html', {'titulo': titulo, 'pessoas': pessoas})

def graficos(request):
	titulo = 'Gráficos Estatísticos por Sexo'
	pessoasM = Pessoa.objects.filter(sexo='M')
	pessoasF = Pessoa.objects.filter(sexo='F')

	salarioM = 0
	for m in pessoasM:
		salarioM += m.salario
	if len(pessoasM) > 0:
		salarioM = salarioM / len(pessoasM)

	salarioF = 0
	for f in pessoasF:
		salarioF += f.salario
	if len(pessoasF) > 0:
		salarioF = salarioF / len(pessoasF)

	idadeM = 0
	for m in pessoasM:
		idadeM += m.idade
	if len(pessoasM) > 0:
		idadeM = idadeM / len(pessoasM)

	idadeF = 0
	for f in pessoasF:
		idadeF += f.idade
	if len(pessoasF) > 0:
		idadeF = idadeF / len(pessoasF)

	return render(request, 'graficos.html', {'titulo': titulo, 'salarioM': salarioM,
											 'salarioF': salarioF,'idadeM':idadeM,'idadeF':idadeF})