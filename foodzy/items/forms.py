from django.forms import ModelForm
from .models import transaction

class foodQueueForm(ModelForm):
    class Meta:       
        model = transaction
        fields = [
            'title',
            'author',
            'recipient',
            'details',
            'want',
            'give',
            'details',
            'tags'
        ]

class foodOfferForm(ModelForm):
    pass