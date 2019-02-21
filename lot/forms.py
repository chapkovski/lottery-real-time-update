from django import forms
from .models import Lottery
from otree.models import Session
from django.forms import ModelChoiceField


class SessionChoiceField(ModelChoiceField):
    """
    This bullshit thing is needed because oTree does not provide any information about Session objects
    """

    def label_from_instance(self, obj):
        return f"{obj.code}"


class LotteryForm(forms.ModelForm):
    """
    Standard form. We just filter out the sessions which have lottery info already.
    """
    session = SessionChoiceField(queryset=Session.objects.filter(lottery__isnull=True))

    class Meta:
        model = Lottery
        fields = ['session', 'input']
