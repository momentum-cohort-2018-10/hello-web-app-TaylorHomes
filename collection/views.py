from django.shortcuts import render
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
