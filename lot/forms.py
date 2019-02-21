from django import forms
from .models import GroupSetting, RoundSetting
from django.forms import modelformset_factory, BaseModelFormSet
from speed import cp


class GroupSetForm(forms.ModelForm):
    class Meta:
        model = GroupSetting
        fields = ['beta', 'gamma']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['beta'] = self.instance.beta
        self.initial['gamma'] = self.instance.gamma


class GroupSetFormset(BaseModelFormSet):
    model = GroupSetting

    def save(self, commit=True):
        s = super().save(commit)
        for i, r in enumerate(GroupSetting.objects.all()):
            r.group_loop_id = i + 1
            r.save()
        return s


group_set_formset = modelformset_factory(GroupSetting,
                                         fields=['beta', 'gamma'],
                                         can_delete=True,
                                         extra=0,
                                         form=GroupSetForm,
                                         formset=GroupSetFormset
                                         )


class RoundSetForm(forms.ModelForm):
    class Meta:
        model = RoundSetting
        fields = ['delta', 'k2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['delta'] = self.instance.delta
        self.initial['k2'] = self.instance.k2


class RoundSetFormset(BaseModelFormSet):
    model = GroupSetting

    def save(self, commit=True):
        s = super().save(commit)
        for i, r in enumerate(GroupSetting.objects.all()):
            r.round = i + 1
            r.save()
        return s


round_set_formset = modelformset_factory(RoundSetting,
                                         fields=['delta', 'k2'],
                                         can_delete=False,
                                         extra=0,
                                         form=RoundSetForm,
                                         formset=RoundSetFormset
                                         )
