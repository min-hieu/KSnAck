from djnago import forms
from .models import transaction

class foodQueueForm(forms.Form):
    title = forms.CharField(default='Help!', max_length=60, )

class foodOfferForm(forms.Form):
    pass