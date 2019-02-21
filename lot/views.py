"""
We
"""

from .models import get_channel_name
from .forms import LotteryForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from channels import Group as ChannelGroup
import json

class LotteryCreate(CreateView):
    success_url = reverse_lazy('DemoIndex')
    url_name = 'insert_lottery_results'
    url_pattern = r'^insert_lottery_results/$'
    form_class = LotteryForm

    template_name = 'lot/admin/InsertLotteryResults.html'

    def form_valid(self, form):
        f = super().form_valid(form)
        self.object.save()
        session = self.object.session
        subsessions = session.get_subsessions()
        # Ph: following lines are not necessary but it's nice to have lottery results exported in standard oTree data
        for s in subsessions:
            s.lottery_result = self.object.input
            s.save()

        group = ChannelGroup(get_channel_name(session))
        group.send(
            {'text': json.dumps({
                'lottery_result': self.object.input,
            })}
        )

        return f
