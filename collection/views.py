from django.shortcuts import render
from collection.models import Villains


def index(request):
    villains = Villains.objects.all()
    return render(request, 'index.html', {
        'villains': villains,
    })
