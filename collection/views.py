from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from collection.forms import VillainForm
from collection.models import Villain
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    villains = Villain.objects.all()
    return render(request, 'index.html', {
        'villains': villains,
    })


def villain_detail(request, slug):
    villain = Villain.objects.get(slug=slug)
    return render(request, 'villains/villain_detail.html', {
        'villain': villain,
    })


def browse_by_name(request, initial=None):
    if initial:
        villains = Villain.objects.filter(
            name__istartswith=initial).order_by('name')
    else:
        villains = Villain.objects.all().order_by('name')
    return render(request, 'search/search.html', {
        'villains': villains,
        'initial': initial,
    })


@login_required
def edit_villain(request, slug):

    villain = Villain.objects.get(slug=slug)
    if villain.user != request.user:
        raise Http404
    form_class = VillainForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=villain)
        if form.is_valid():
            form.save()
            return redirect('villain_detail', slug=villain.slug)
    else:
        form = form_class(instance=villain)

    return render(request, 'villains/edit_villain.html', {
        'villain': villain,
        'form': form,
    })


def create_villain(request):
    form_class = VillainForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            villain = form.save(commit=False)
            villain.user = request.user
            villain.slug = slugify(villain.name)
            villain.save()
            return redirect('villain_detail', slug=villain.slug)
    else:
        form = form_class()
    return render(request, 'villains/create_villain.html', {
        'form': form,
    })
