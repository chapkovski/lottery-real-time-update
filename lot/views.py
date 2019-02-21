from django.views.generic import UpdateView
from speed.models import GroupSetting, prepopulate_group_settings, RoundSetting, prepopulate_round_settings
from .forms import  GroupSetForm, RoundSetForm, group_set_formset, round_set_formset
from django.views.generic import FormView, CreateView
from . import cp
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
from django.db.models import Max


class GroupSetView(FormView):
    template_name = 'speed/admin/GroupSettings.html'
    url_name = 'speed_group_settings'
    url_pattern = r'^speed_group_settings/$'
    display_name = 'Settings for a group (beta, gamma...)'
    form_class = GroupSetForm
    formset_class = group_set_formset
    success_url = reverse_lazy('ExportIndex')

    def get_queryset(self):
        return GroupSetting.objects.all()

    def get_context_data(self, bounded_formset=None, **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.get_queryset()
        if bounded_formset:
            formset = bounded_formset
        else:
            formset = self.formset_class(queryset=q)
        context['formset'] = formset
        context['title'] = 'Group settings'
        return context

    def post(self, request, *args, **kwargs):
        q = self.get_queryset()
        formset = self.formset_class(self.request.POST, queryset=q)
        if not formset.is_valid():
            context = self.get_context_data(bounded_formset=formset)
            context['formset'] = formset
            return self.render_to_response(context)
        formset.save()
        return self.form_valid(formset)


class PrepopulateGroupSView(RedirectView):
    url = reverse_lazy('speed_group_settings')
    url_name = 'prepopulate_group_settings'
    url_pattern = r'^prepopulate_group_settings/$'

    def get_redirect_url(self, *args, **kwargs):
        prepopulate_group_settings()
        return super().get_redirect_url(*args, **kwargs)


class GroupSCreate(CreateView):
    success_url = reverse_lazy('speed_group_settings')
    url_name = 'create_group_setting'
    url_pattern = r'^create_group_setting/$'
    model = GroupSetting
    fields = ['beta', 'gamma']
    template_name = 'speed/admin/CreateGroupSettings.html'

    def form_valid(self, form):
        f = super().form_valid(form)
        n = self.model.objects.all().aggregate(max_round=Max('round'))['max_round']
        if n:
            self.object.group_loop_id = n + 1
        else:
            self.object.group_loop_id = 1
        self.object.save()
        return f


########### BLOCK: Round settings views ##############################################################

class RoundSetView(FormView):
    template_name = 'speed/admin/RoundSettings.html'
    url_name = 'speed_round_settings'
    url_pattern = r'^speed_round_settings/$'
    display_name = 'Settings for a round (delta, k2...)'
    form_class = RoundSetForm
    formset_class = round_set_formset
    success_url = reverse_lazy('ExportIndex')

    def get_queryset(self):
        return RoundSetting.objects.all()

    # TODO; move to upper class with formset!
    # TOdo: check parameters for sanity!!!
    def get_context_data(self, bounded_formset=None, **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.get_queryset()
        if bounded_formset:
            formset = bounded_formset
        else:
            formset = self.formset_class(queryset=q)
        context['formset'] = formset
        context['title'] = 'Round settings'
        return context

    # TODO; move to upper class with formset!

    def post(self, request, *args, **kwargs):
        q = self.get_queryset()
        formset = self.formset_class(self.request.POST, queryset=q)
        if not formset.is_valid():
            context = self.get_context_data(bounded_formset=formset)
            context['formset'] = formset
            return self.render_to_response(context)
        formset.save()
        return self.form_valid(formset)


class PrepopulateRoundSView(RedirectView):
    url = reverse_lazy('speed_round_settings')
    url_name = 'prepopulate_round_settings'
    url_pattern = r'^prepopulate_round_settings/$'

    def get_redirect_url(self, *args, **kwargs):
        prepopulate_round_settings()
        return super().get_redirect_url(*args, **kwargs)


############ END OF: Round settings views #############################################################
