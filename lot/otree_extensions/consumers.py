import json
from channels.generic.websockets import JsonWebsocketConsumer
from otree.models import Participant
from lot.models import Player, get_channel_name
from utils import cp


class LotteryTracker(JsonWebsocketConsumer):
    url_pattern = (r'^/lottery_channel/(?P<player_pk>[0-9]+)$')

    def clean_kwargs(self):
        self.player_pk = self.kwargs['player_pk']

    def connection_groups(self, **kwargs):
        subsession_channel = get_channel_name(self.get_player().session)
        return [subsession_channel]

    def get_player(self):
        self.clean_kwargs()
        return Player.objects.get(pk=self.player_pk)

    def receive(self, content, **kwargs):
        raw_content = json.loads(content)
        # just some sanity check
        result = raw_content['result']
        cp('RESULT!!', result)

    def connect(self, message, **kwargs):
        # just some sanity check
        p = self.get_player()
        cp(p.subsession.lottery_result, '::: RESULT!?')
        print('Connected to lottery tracker...')

    def disconnect(self, message, **kwargs):
        # just some sanity check
        print('client disconnected from lottery tracker...')
