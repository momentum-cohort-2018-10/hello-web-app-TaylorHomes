from django.forms import ModelForm
from collection.models import Villain


class VillainForm(ModelForm):
    class Meta:
        model = Villain
        fields = (
            'name',
            'description',
        )
