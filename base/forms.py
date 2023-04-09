from django.forms import ModelForm
from .models import Opinion

class OpinionForm(ModelForm):
    class Meta:
        model = Opinion
        fields = '__all__'
        exclude = ['user']