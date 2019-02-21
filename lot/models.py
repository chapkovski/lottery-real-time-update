from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.db import models as djmodels
from otree.models import Session
from utils import cp

author = 'Your name here'

doc = """
Your app description
"""


def get_channel_name(session: Session) -> str:
    return f'session_{session.code}'


class Constants(BaseConstants):
    name_in_url = 'lot'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    lottery_result = models.IntegerField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class Lottery(djmodels.Model):
    input = models.IntegerField()
    session = djmodels.OneToOneField(to=Session, related_name='lottery')
