from django.shortcuts import render
from collection.models import Villain


def index(request):
    villains = Villain.objects.all()
    return render(request, 'index.html', {
        'villains': villains,
    })
