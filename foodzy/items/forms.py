from django.forms import ModelForm
from django.forms import ChoiceField
from django.forms import RadioSelect
from .models import transaction
from django.utils.safestring import mark_safe

class HorizontalRadioRenderer(RadioSelect):
    def render(self,renderer=None):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class foodQueueForm(ModelForm):

    class Meta:       
        model = transaction
        fields = [
            'title',
            'author',
            'content',
            'details',
            'tags',
            'method'
        ]