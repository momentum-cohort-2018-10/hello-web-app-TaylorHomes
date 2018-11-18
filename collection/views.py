from django.shortcuts import render, redirect
from collection.forms import VillainForm
from collection.models import Villain


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


def edit_villain(request, slug):

    villain = Villain.objects.get(slug=slug)
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
