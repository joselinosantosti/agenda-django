from django.shortcuts import render, get_object_or_404, redirect
from.models import Contato
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    contatos = Contato.objects.order_by('id').filter(mostrar=True)
    paginator = Paginator(contatos, 10)
    page = request.GET.get('p')
    total = request.GET.get('total')
    contatos = paginator.get_page(page)
    
    return render(request, 'contatos/index.html', {
        'contatos':contatos
    })

@login_required()
def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.mostrar:
        raise Http404
    return render(request, 'contatos/contato.html', {
        'contato':contato
    })

@login_required()
def busca(request):
    busca = request.GET.get('busca')
    
    if busca is None or not busca:
        messages.add_message(request, messages.ERROR, 'Campo pesquisa não pode ser vazio.')
        return redirect('index')
        #raise Http404()

    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects.annotate(
        nome_completo = campos
    ).order_by('id').filter(Q(nome_completo__icontains = busca) | Q(telefone__icontains = busca), mostrar=True)
    paginator = Paginator(contatos, 5)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    
    return render(request, 'contatos/busca.html', {
        'contatos':contatos
    })