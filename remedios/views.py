from django.shortcuts import render, get_object_or_404, redirect
from remedios.models import Remedio
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.http import Http404
from django.contrib import messages


def index(request):
    # filtra (mostra) os remedios da classe criada no models.py
    remedios = Remedio.objects.order_by('-id')

    paginator = Paginator(remedios, 5)
    page = request.GET.get('p')
    remedios = paginator.get_page(page)

    return render(request, 'remedios/index.html', {'remedios': remedios})


def ver_remedio(request, remedio_id):
    remedio = get_object_or_404(Remedio, id=remedio_id)
    return render(request, 'remedios/ver_remedio.html', {'remedio': remedio})


def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(request,
                             messages.ERROR,
                             'Campo busca não pode ficar vazio.'
                             )
        return redirect('index')

    campos = Concat('nome', Value(' '), 'dosagem')

    remedios = Remedio.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(dosagem__icontains=termo)
    )
    paginator = Paginator(remedios, 5)

    page = request.GET.get('p')
    remedios = paginator.get_page(page)

    return render(request, 'remedios/index.html', {'remedios': remedios})