from django.shortcuts import render, get_object_or_404, redirect
from.models import Empregado
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    empregados = Empregado.objects.order_by('id').filter(mostrar=True)
    paginator = Paginator(empregados, 10)
    page = request.GET.get('p')
    total = request.GET.get('total')
    empregados = paginator.get_page(page)
    
    return render(request, 'empregados/index.html', {
        'empregados':empregados
    })

@login_required()
def empregado(request, Empregado_id):
    Empregado = get_object_or_404(Empregado, id=Empregado_id)
    if not Empregado.mostrar:
        raise Http404
    return render(request, 'empregados/Empregado.html', {
        'Empregado':Empregado
    })

@login_required()
def busca(request):
    busca = request.GET.get('busca')
    
    if busca is None or not busca:
        messages.add_message(request, messages.ERROR, 'Campo pesquisa não pode ser vazio.')
        return redirect('index')
        #raise Http404()

    campos = Concat('nome', Value(' '), 'sobrenome')

    empregados = Empregado.objects.annotate(
        nome_completo = campos
    ).order_by('id').filter(Q(nome_completo__icontains = busca) | Q(telefone__icontains = busca), mostrar=True)
    paginator = Paginator(empregados, 5)
    page = request.GET.get('p')
    empregados = paginator.get_page(page)
    
    return render(request, 'empregados/busca.html', {
        'empregados':empregados
    })