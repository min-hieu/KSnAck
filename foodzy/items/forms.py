from django.forms import ModelForm
from django.forms import ChoiceField
from django.forms import RadioSelect
from .models import transaction
from django.utils.safestring import mark_safe

class HorizontalRadioRenderer(RadioSelect):
    def render(self,renderer=None):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class foodQueueForm(ModelForm):

    CHOICES=[(0,'request'),
             (1,'offer')]

    method = ChoiceField(
        choices=CHOICES,
        widget=RadioSelect(),
        )

    class Meta:       
        model = transaction
        fields = [
            'title',
            'author',
            'content',
            'details',
            'tags'
        ]