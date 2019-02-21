from django import forms
from .models import Lottery
from otree.models import Session
from utils import cp

from django.forms import ModelChoiceField

class SessionChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.code}"

class LotteryForm(forms.ModelForm):
    session = SessionChoiceField(queryset=Session.objects.filter(lottery__isnull=True))
    class Meta:
        model = Lottery
        fields = ['session', 'input']



