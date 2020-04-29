"""Character class.

Define perks for characters.
"""
from cards import Card
from perks import Perk


class Character_Class:
    """Character_Class definition."""

    def __init__(self, character_class):
        """Initialize attributes."""
        self.character_class = character_class
        self.perks = []
        self.determine_perks()

    def determine_perks(self):
        """Determine what perks the character has access to."""
        class_perks = class_dictionary[self.character_class]
        for perk in class_perks:
            self.perks.append(perk)


# description='', add=[], remove=[]
# [
#         Perk(description="", add=[], remove=[]),
#         Perk(description="", add=[], remove=[]),
#         Perk(description="", add=[], remove=[]),
#         Perk(description="", add=[], remove=[]),
#         Perk(description="", add=[], remove=[]),
#         Perk(description="", add=[], remove=[]),
#         Perk(description="", add=[], remove=[]),
#         Perk(description="", add=[], remove=[]),
#         Perk(description="", add=[], remove=[]),
#         Perk(description="", add=[], remove=[]),
#         Perk(description="", add=[], remove=[]),
#         Perk(description="", add=[], remove=[]),
#         Perk(description="", add=[], remove=[]),
#         Perk(description="", add=[], remove=[]),
#         Perk(description="", add=[], remove=[])
# ]
brute_perks = [
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Replace one -1 card with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Add two +1 cards", add=[Card(value=1), Card(value=1)]),
    Perk(description="Add two +1 cards", add=[Card(value=1), Card(value=1)]),
    Perk(description="Add one +3 card", add=[Card(value=3)]),
    Perk(description="Add 3 rolling Push 1 cards", add=[
        Card(status_effect="push1", is_rolling=True),
        Card(status_effect="push1", is_rolling=True),
        Card(status_effect="push1", is_rolling=True)]),
    Perk(description="Add 3 rolling Push 1 cards", add=[
        Card(status_effect="push1", is_rolling=True),
        Card(status_effect="push1", is_rolling=True),
        Card(status_effect="push1", is_rolling=True)]),
    Perk(description="Add two rolling Pierce 3 cards", add=[
        Card(is_rolling=True, status_effect="pierce3"),
        Card(is_rolling=True, status_effect="pierce3")]),
    Perk(description="Add one rolling Stun card", add=[
        Card(is_rolling=True, status_effect="stun")]),
    Perk(description="Add one rolling Stun card", add=[
        Card(is_rolling=True, status_effect="stun")]),
    Perk(description="Add one rolling Disarm card and one rolling Muddle card",
         add=[Card(is_rolling=True, status_effect="disarm"),
              Card(is_rolling=True, status_effect="muddle")]),
    Perk(description="Add one rolling Add Target card", add=[
        Card(is_rolling=True, status_effect="target")]),
    Perk(description="Add one rolling Add Target card", add=[
        Card(is_rolling=True, status_effect="target")]),
    Perk(description="Add one +1 Shield 1, Self card", add=[
        Card(value=1, status_effect="shield_self1")]),
    Perk(description="Ignore negative item effects and add one +1 card",
         add=[Card(value=1)], remove=[]),
]

tinkerer_perks = [
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Replace one -2 card with one +0 card",
         add=[Card(value=0)], remove=[-2]),
    Perk(description="Add two +1 cards",
         add=[Card(value=1), Card(value=1)]),
    Perk(description="Add one +3 card", add=[Card(value=3)]),
    Perk(description="Add two rolling Fire cards", add=[
        Card(value=0, element="fire", is_rolling=True),
        Card(value=0, element="fire", is_rolling=True)]),
    Perk(description="Add three rolling Muddle cards", add=[
        Card(status_effect="muddle", is_rolling=True),
        Card(status_effect="muddle", is_rolling=True),
        Card(status_effect="muddle", is_rolling=True)]),
    Perk(description="Add one +1 Wound card", add=[
        Card(value=1, status_effect="wound")]),
    Perk(description="Add one +1 Wound card", add=[
        Card(value=1, status_effect="wound")]),
    Perk(description="Add one +1 Immobilize card",
         add=[Card(value=1, status_effect="immobilize")]),
    Perk(description="Add one +1 Immobilize card",
         add=[Card(value=1, status_effect="immobilize")]),
    Perk(description="Add one +1 Heal 2 card",
         add=[Card(value=1, status_effect="heal_self2")]),
    Perk(description="Add one +1 Heal 2 card",
         add=[Card(value=1, status_effect="heal_self2")]),
    Perk(description="Add one +0 Add Target card",
         add=[Card(status_effect="target")]),
    Perk(description="Ignore negative scenario effects")
]
spellweaver_perks = [
    Perk(description="Remove four +0 cards", add=[], remove=[0, 0, 0, 0]),
    Perk(description="Replace one -1 card with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Replace one -1 card with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Add two +1 cards", add=[Card(value=1), Card(value=1)]),
    Perk(description="Add two +1 cards", add=[Card(value=1), Card(value=1)]),
    Perk(description="Add one +0 Stun card", add=[Card(status_effect="stun")]),
    Perk(description="Add one +1 Wound card",
         add=[Card(value=1, status_effect="wound")]),
    Perk(description="Add one +1 Immobilize card",
         add=[Card(value=1, status_effect="immobilize")]),
    Perk(description="Add one +1 Curse card",
         add=[Card(value=1, status_effect="curse")]),
    Perk(description="Add one +2 Fire card",
         add=[Card(value=2, element="fire")]),
    Perk(description="Add one +2 Fire card",
         add=[Card(value=2, element="fire")]),
    Perk(description="Add one +2 Ice card",
         add=[Card(value=2, element="ice")]),
    Perk(description="Add one +2 Ice card",
         add=[Card(value=2, element="ice")]),
    Perk(description="Add one rolling Earth card and one rolling Wind card",
         add=[Card(is_rolling=True, element="earth"),
              Card(is_rolling=True, element="wind")]),
    Perk(description="Add one rolling Light card and one rolling Dark card",
         add=[Card(is_rolling=True, element="light"),
              Card(is_rolling=True, element="dark")])
]
cragheart_perks = [
    Perk(description="Remove four +0 cards", remove=[0, 0, 0, 0]),
    Perk(description="Replace one -1 card with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Replace one -1 card with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Replace one -1 card with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Add one -2 card and two +2 cards",
         add=[Card(value=2), Card(value=2), Card(value=-2)]),
    Perk(description="Add one +1 Immobilize card",
         add=[Card(value=1, status_effect="immobilize")]),
    Perk(description="Add one +1 Immobilize card",
         add=[Card(value=1, status_effect="immobilize")]),
    Perk(description="Add one +2 Muddle card",
         add=[Card(value=2, status_effect="muddle")]),
    Perk(description="Add one +2 Muddle card",
         add=[Card(value=2, status_effect="muddle")]),
    Perk(description="Add two rolling Push 2 cards", add=[
        Card(is_rolling=True, status_effect="push2"),
        Card(is_rolling=True, status_effect="push2")]),
    Perk(description="Add two rolling Earth cards", add=[
         Card(is_rolling=True, element="earth"),
         Card(is_rolling=True, element="earth")]),
    Perk(description="Add two rolling Earth cards", add=[
         Card(is_rolling=True, element="earth"),
         Card(is_rolling=True, element="earth")]),
    Perk(description="Add two rolling Wind cards", add=[
         Card(is_rolling=True, element="wind"),
         Card(is_rolling=True, element="wind")]),
    Perk(description="Ignore negative item effects"),
    Perk(description="Ignore negative scenario effects")
]
scoundrel_perks = [
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove four +0 cards", add=[], remove=[0, 0, 0, 0]),
    Perk(description="Replace one -2 card with one +0 card",
         add=[Card(value=0)], remove=[-2]),
    Perk(description="Replace one -1 card with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Replace one +0 card with one +2 card",
         add=[Card(value=2)], remove=[0]),
    Perk(description="Replace one +0 card with one +2 card",
         add=[Card(value=2)], remove=[0]),
    Perk(description="Add two rolling +1 cards", add=[
        Card(is_rolling=True, value=1),
        Card(is_rolling=True, value=1)]),
    Perk(description="Add two rolling +1 cards", add=[
        Card(is_rolling=True, value=1), Card(is_rolling=True, value=1)]),
    Perk(description="Add two rolling Pierce 3 cards", add=[
        Card(is_rolling=True, status_effect="pierce3"),
        Card(is_rolling=True, status_effect="pierce3")]),
    Perk(description="Add two rolling Poison cards", add=[
        Card(is_rolling=True, status_effect="poison"),
        Card(is_rolling=True, status_effect="poison")]),
    Perk(description="Add two rolling Poison cards", add=[
        Card(is_rolling=True, status_effect="poison"),
        Card(is_rolling=True, status_effect="poison")]),
    Perk(description="Add two rolling Muddle cards", add=[
        Card(is_rolling=True, status_effect="muddle"),
        Card(is_rolling=True, status_effect="muddle")]),
    Perk(description="Add one rolling Invisible card", add=[
        Card(is_rolling=True, status_effect="invisible")]),
    Perk(description="Ignore negative scenario effects", add=[], remove=[])
]
mindtheif_perks = [
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove four +0 cards", remove=[0, 0, 0, 0]),
    Perk(description="Replace two +1 cards with two +2 cards", add=[
        Card(value=2), Card(value=2)], remove=[1, 1]),
    Perk(description="Replace one -2 card with one +0 card", add=[
        Card(value=0)], remove=[-2]),
    Perk(description="Add one +2 Ice card", add=[
        Card(value=2, element="ice")]),
    Perk(description="Add one +2 Ice card", add=[
        Card(value=2, element="ice")]),
    Perk(description="Add two rolling +1 cards", add=[
        Card(is_rolling=True, value=1), Card(is_rolling=True, value=1)]),
    Perk(description="Add two rolling +1 cards", add=[
        Card(is_rolling=True, value=1), Card(is_rolling=True, value=1)]),
    Perk(description="Add three rolling Pull 1 cards", add=[
        Card(is_rolling=True, status_effect="pull1"),
        Card(is_rolling=True, status_effect="pull1"),
        Card(is_rolling=True, status_effect="pull1")]),
    Perk(description="Add three rolling Muddle cards", add=[
        Card(is_rolling=True, status_effect="muddle"),
        Card(is_rolling=True, status_effect="muddle"),
        Card(is_rolling=True, status_effect="muddle")]),
    Perk(description="Add two rolling Immobilize cards", add=[
        Card(is_rolling=True, status_effect="immobilize"),
        Card(is_rolling=True, status_effect="immobilize")]),
    Perk(description="Add one rolling Stun card", add=[
        Card(is_rolling=True, status_effect="stun")]),
    Perk(description="Add one rolling Disarm card and one rolling Muddle card",
         add=[Card(is_rolling=True, status_effect="disarm"),
              Card(is_rolling=True, status_effect="muddle")]),
    Perk(description="Ignore negative scenario effects", add=[], remove=[])
]
sunkeeper_perks = [
    Perk(description="Remove two -1 cards", add=[], remove=[-1, -1]),
    Perk(description="Remove two -1 cards", add=[], remove=[-1, -1]),
    Perk(description="Remove four +0 cards", add=[], remove=[0, 0, 0, 0]),
    Perk(description="Replace one -2 card with one +0 card",
         add=[Card(value=0)], remove=[-2]),
    Perk(description="Replace one +0 card with one +2 card",
         add=[Card(value=2)], remove=[0]),
    Perk(description="Add two rolling +1 cards", add=[
        Card(is_rolling=True, value=1), Card(is_rolling=True, value=1)]),
    Perk(description="Add two rolling +1 cards", add=[
        Card(is_rolling=True, value=1), Card(is_rolling=True, value=1)]),
    Perk(description="Add two rolling Heal 1 cards", add=[
        Card(is_rolling=True, status_effect="heal_self1"),
        Card(is_rolling=True, status_effect="heal_self1")]),
    Perk(description="Add two rolling Heal 1 cards", add=[
        Card(is_rolling=True, status_effect="heal_self1"),
        Card(is_rolling=True, status_effect="heal_self1")]),
    Perk(description="Add one rolling Stun card", add=[
        Card(is_rolling=True, status_effect="stun")]),
    Perk(description="Add two rolling Light cards", add=[
        Card(is_rolling=True, element="light"),
        Card(is_rolling=True, element="light")]),
    Perk(description="Add two rolling Light cards", add=[
        Card(is_rolling=True, element="light"),
        Card(is_rolling=True, element="light")]),
    Perk(description="Add two rolling Shield 1, Self cards", add=[
        Card(is_rolling=True, status_effect="shield_self1"),
        Card(is_rolling=True, status_effect="shield_self1")]),
    Perk(description="Ignore negative item effects and add two +1 cards",
         add=[Card(value=1), Card(value=1)]),
    Perk(description="Ignore negative scenario effects")
]
quartermaster_perks = [
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove four +0 cards", remove=[0, 0, 0, 0]),
    Perk(description="Replace one +0 card with one +2 card", add=[
        Card(value=2)], remove=[0]),
    Perk(description="Replace one +0 card with one +2 card", add=[
        Card(value=2)], remove=[0]),
    Perk(description="Add two rolling +1 cards", add=[
        Card(is_rolling=True, value=1), Card(is_rolling=True, value=1)]),
    Perk(description="Add two rolling +1 cards", add=[
        Card(is_rolling=True, value=1), Card(is_rolling=True, value=1)]),
    Perk(description="Add three rolling Muddle cards", add=[
        Card(is_rolling=True, status_effect="muddle"),
        Card(is_rolling=True, status_effect="muddle"),
        Card(is_rolling=True, status_effect="muddle")]),
    Perk(description="Add two rolling Pierce 3 cards", add=[
        Card(is_rolling=True, status_effect="pierce3"),
        Card(is_rolling=True, status_effect="pierce3")]),
    Perk(description="Add one rolling Stun card", add=[
        Card(is_rolling=True, status_effect="stun")], remove=[]),
    Perk(description="Add one rolling Add Target card", add=[
        Card(is_rolling=True, status_effect="target")]),
    Perk(description="Add one +0 Refresh an Item card", add=[
        Card(status_effect="item")]),
    Perk(description="Add one +0 Refresh an Item card", add=[
        Card(status_effect="item")]),
    Perk(description="Add one +0 Refresh an Item card", add=[
        Card(status_effect="item")]),
    Perk(description="Ignore negative item effects and add two +1 cards",
         add=[Card(value=1), Card(value=1)])
]
summoner_perks = [
    Perk(description="Remove two -1 cards", add=[], remove=[-1, -1]),
    Perk(description="Replace one -2 card with one +0 card",
         add=[Card(value=0)], remove=[-2]),
    Perk(description="Replace one -1 card with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Replace one -1 card with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Replace one -1 card with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Add one +2 card", add=[Card(value=2)]),
    Perk(description="Add one +2 card", add=[Card(value=2)]),
    Perk(description="Add two rolling Wound cards",
         add=[Card(is_rolling=True, status_effect="wound"),
              Card(is_rolling=True, status_effect="wound")]),
    Perk(description="Add two rolling Poison cards",
         add=[Card(is_rolling=True, status_effect="poison"),
              Card(is_rolling=True, status_effect="poison")]),
    Perk(description="Add two rolling Heal 1 cards",
         add=[Card(is_rolling=True, status_effect="heal_self1"),
              Card(is_rolling=True, status_effect="heal_self1")]),
    Perk(description="Add two rolling Heal 1 cards",
         add=[Card(is_rolling=True, status_effect="heal_self1"),
              Card(is_rolling=True, status_effect="heal_self1")]),
    Perk(description="Add two rolling Heal 1 cards",
         add=[Card(is_rolling=True, status_effect="heal_self1"),
              Card(is_rolling=True, status_effect="heal_self1")]),
    Perk(description="Add one rolling Fire card and one rolling Wind card",
         add=[Card(is_rolling=True, element="fire"),
              Card(is_rolling=True, element="wind")]),
    Perk(description="Add one rolling Dark card and one rolling Earth card",
         add=[Card(is_rolling=True, element="dark"),
              Card(is_rolling=True, element="earth")]),
    Perk(description="Ignore negative scenario effects and add two +1 cards",
         add=[Card(value=1), Card(value=1)])
]
nightshroud_perks = [
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove four +0 cards", remove=[0, 0, 0, 0]),
    Perk(description="Add one -1 Dark card",
         add=[Card(value=-1, element="dark")]),
    Perk(description="Add one -1 Dark card",
         add=[Card(value=-1, element="dark")]),
    Perk(description="Replace one -1 Dark card with one +1 Dark card",
         add=[Card(value=1, element="dark")],
         remove=["nightshroud_minus_one_dark"]),
    Perk(description="Replace one -1 Dark card with one +1 Dark card",
         add=[Card(value=1, element="dark")],
         remove=["nightshroud_minus_one_dark"]),
    Perk(description="Add one +1 Invisible card",
         add=[Card(value=1, status_effect="invisible")]),
    Perk(description="Add one +1 Invisible card",
         add=[Card(value=1, status_effect="invisible")]),
    Perk(description="Add three rolling Muddle cards",
         add=[Card(is_rolling=True, status_effect="muddle"),
              Card(is_rolling=True, status_effect="muddle"),
              Card(is_rolling=True, status_effect="muddle")]),
    Perk(description="Add three rolling Muddle cards",
         add=[Card(is_rolling=True, status_effect="muddle"),
              Card(is_rolling=True, status_effect="muddle"),
              Card(is_rolling=True, status_effect="muddle")]),
    Perk(description="Add two rolling Heal 1 cards",
         add=[Card(is_rolling=True, status_effect="heal_self1"),
              Card(is_rolling=True, status_effect="heal_self1")]),
    Perk(description="Add two rolling Curse cards",
         add=[Card(is_rolling=True, status_effect="curse"),
              Card(is_rolling=True, status_effect="curse")]),
    Perk(description="Add one rolling Add Target card",
         add=[Card(is_rolling=True, status_effect="target")]),
    Perk(description="Ignore negative scenario effects and add two +1 cards",
         add=[Card(value=1), Card(value=1)])
]
plagueherald_perks = [
    Perk(description="Replace one -2 card with one +0 card",
         add=[Card(value=0)], remove=[-2]),
    Perk(description="Replace one -1 card with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Replace one -1 card with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Replace one +0 card with one +2 card",
         add=[Card(value=2)], remove=[0]),
    Perk(description="Replace one +0 card with one +2 card",
         add=[Card(value=2)], remove=[0]),
    Perk(description="Add two +1 cards", add=[Card(value=1), Card(value=1)]),
    Perk(description="Add one +1 Wind card",
         add=[Card(value=1, element="wind")]),
    Perk(description="Add one +1 Wind card",
         add=[Card(value=1, element="wind")]),
    Perk(description="Add one +1 Wind card",
         add=[Card(value=1, element="wind")]),
    Perk(description="Add three rolling Poison cards",
         add=[Card(is_rolling=True, status_effect="poison"),
              Card(is_rolling=True, status_effect="poison"),
              Card(is_rolling=True, status_effect="poison")]),
    Perk(description="Add two rolling Curse cards",
         add=[Card(is_rolling=True, status_effect="curse"),
              Card(is_rolling=True, status_effect="curse")]),
    Perk(description="Add two Immobilize cards",
         add=[Card(status_effect="immobilize"),
              Card(status_effect="immobilize")]),
    Perk(description="Add one Stun card", add=[Card(status_effect="stun")]),
    Perk(description="Add one Stun card", add=[Card(status_effect="stun")]),
    Perk(description="Ignore negative scenario effects and add one +1 card",
         add=[Card(value=1)])
]
berserker_perks = [
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove four +0 cards", remove=[0, 0, 0, 0]),
    Perk(description="Replace one -1 cand with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Replace one -1 cand with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Replace one +0 card with one rolling +2 card",
         add=[Card(value=2)], remove=[0]),
    Perk(description="Replace one +0 card with one rolling +2 card",
         add=[Card(value=2)], remove=[0]),
    Perk(description="Add two rolling Wound cards",
         add=[Card(is_rolling=True, status_effect="wound"),
              Card(is_rolling=True, status_effect="wound")]),
    Perk(description="Add two rolling Wound cards",
         add=[Card(is_rolling=True, status_effect="wound"),
              Card(is_rolling=True, status_effect="wound")]),
    Perk(description="Add one rolling Stun card",
         add=[Card(is_rolling=True, status_effect="stun")]),
    Perk(description="Add one rolling Stun card",
         add=[Card(is_rolling=True, status_effect="stun")]),
    Perk(description="Add one rolling +1 Disarm card",
         add=[Card(is_rolling=True, value=1, status_effect="disarm")]),
    Perk(description="Add two rolling Heal 1 cards",
         add=[Card(is_rolling=True, status_effect="heal_self1"),
              Card(is_rolling=True, status_effect="heal_self1")]),
    Perk(description="Add one +2 Fire card",
         add=[Card(value=2, element="fire")]),
    Perk(description="Add one +2 Fire card",
         add=[Card(value=2, element="fire")]),
    Perk(description="Ignore negative item effects")
]
soothsinger_perks = [
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove one -2 card", remove=[-2]),
    Perk(description="Replace two +1 cards with one +4 card",
         add=[Card(value=4)], remove=[1, 1]),
    Perk(description="Replace two +1 cards with one +4 card",
         add=[Card(value=4)], remove=[1, 1]),
    Perk(description="Replace one +0 card with one +1 Immobilize card",
         add=[Card(value=1, status_effect="immobilize")], remove=[0]),
    Perk(description="Replace one +0 card with one +1 Disarm card",
         add=[Card(value=1, status_effect="disarm")], remove=[0]),
    Perk(description="Replace one +0 card with one +2 Wound card",
         add=[Card(value=2, status_effect="wound")], remove=[0]),
    Perk(description="Replace one +0 card with one +2 Poison card",
         add=[Card(value=2, status_effect="poison")], remove=[0]),
    Perk(description="Replace one +0 card with one +2 Curse card",
         add=[Card(value=2, status_effect="curse")], remove=[0]),
    Perk(description="Replace one +0 card with one +3 Muddle card",
         add=[Card(value=3, status_effect="muddle")], remove=[0]),
    Perk(description="Replace one -1 card with one +0 Stun card",
         add=[Card(status_effect="stun")], remove=[0]),
    Perk(description="Add three rolling +1 cards",
         add=[Card(is_rolling=True, value=1),
              Card(is_rolling=True, value=1),
              Card(is_rolling=True, value=1)]),
    Perk(description="Add two rolling Curse cards",
         add=[Card(is_rolling=True, status_effect="curse"),
              Card(is_rolling=True, status_effect="curse")]),
    Perk(description="Add two rolling Curse cards",
         add=[Card(is_rolling=True, status_effect="curse"),
              Card(is_rolling=True, status_effect="curse")])
]
doomstalker_perks = [
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Replace two +0 cards with two +1 cards",
         add=[Card(value=1), Card(value=1)], remove=[0, 0]),
    Perk(description="Replace two +0 cards with two +1 cards",
         add=[Card(value=1), Card(value=1)], remove=[0, 0]),
    Perk(description="Replace two +0 cards with two +1 cards",
         add=[Card(value=1), Card(value=1)], remove=[0, 0]),
    Perk(description="Add two rolling +1 cards",
         add=[Card(is_rolling=True, value=1), Card(is_rolling=True, value=1)]),
    Perk(description="Add two rolling +1 cards",
         add=[Card(is_rolling=True, value=1), Card(is_rolling=True, value=1)]),
    Perk(description="Add one +2 Muddle card",
         add=[Card(value=2, status_effect="muddle")]),
    Perk(description="Add one +1 Poison card",
         add=[Card(value=1, status_effect="poison")]),
    Perk(description="Add one +1 Wound card",
         add=[Card(value=1, status_effect="wound")]),
    Perk(description="Add one +1 Immobilize card",
         add=[Card(value=1, status_effect="immobilize")]),
    Perk(description="Add one +0 Stun card", add=[Card(status_effect="stun")]),
    Perk(description="Add one rolling Add Target card", add=[
         Card(is_rolling=True, status_effect="target")]),
    Perk(description="Add one rolling Add Target card", add=[
         Card(is_rolling=True, status_effect="target")]),
    Perk(description="Ignore negative scenario effects")
]
sawbones_perks = [
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove four +0 cards", remove=[0, 0, 0, 0]),
    Perk(description="Replace one +0 card with one +2 card",
         add=[Card(value=2)], remove=[0]),
    Perk(description="Replace one +0 card with one +2 card",
         add=[Card(value=2)], remove=[0]),
    Perk(description="Add one rolling +2 card",
         add=[Card(is_rolling=True, value=2)]),
    Perk(description="Add one rolling +2 card",
         add=[Card(is_rolling=True, value=2)]),
    Perk(description="Add one +1 Immobilize card",
         add=[Card(value=1, status_effect="immobilize")]),
    Perk(description="Add one +1 Immobilize card",
         add=[Card(value=1, status_effect="immobilize")]),
    Perk(description="Add two rolling Wound cards",
         add=[Card(is_rolling=True, status_effect="wound"),
              Card(is_rolling=True, status_effect="wound")]),
    Perk(description="Add two rolling Wound cards",
         add=[Card(is_rolling=True, status_effect="wound"),
              Card(is_rolling=True, status_effect="wound")]),
    Perk(description="Add one rolling Stun card",
         add=[Card(is_rolling=True, status_effect="stun")]),
    Perk(description="Add one rolling Heal 3 card",
         add=[Card(is_rolling=True, status_effect="heal_self3")]),
    Perk(description="Add one rolling Heal 3 card",
         add=[Card(is_rolling=True, status_effect="heal_self3")]),
    Perk(description="Add one +0 Refresh an Item card",
         add=[Card(status_effect="item")])
]
elementalist_perks = [
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Replace one -1 card with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Replace one +0 card with one +2 card",
         add=[Card(value=2)], remove=[0]),
    Perk(description="Replace one +0 card with one +2 card",
         add=[Card(value=2)], remove=[0]),
    Perk(description="Add three +0 Fire cards",
         add=[Card(element="fire"),
              Card(element="fire"),
              Card(element="fire")]),
    Perk(description="Add three +0 Ice cards",
         add=[Card(element="ice"),
              Card(element="ice"),
              Card(element="ice")]),
    Perk(description="Add three +0 Wind cards",
         add=[Card(element="wind"),
              Card(element="wind"),
              Card(element="wind")]),
    Perk(description="Add three +0 Earth cards",
         add=[Card(element="earth"),
              Card(element="earth"),
              Card(element="earth")]),
    Perk(description="Replace two +0 cards with \
    one +0 Fire card and one +0 Earth card",
         add=[Card(element="fire"), Card(element="earth")], remove=[0, 0]),
    Perk(description="Replace two +0 cards with one +0 Ice card\
    and one +0 Wind card",
         add=[Card(element="ice"), Card(element="wind")], remove=[0, 0]),
    Perk(description="Add two +1 Push 1 cards",
         add=[Card(value=1, status_effect="push1"),
              Card(value=1, status_effect="push1")]),
    Perk(description="Add one +1 Wound card",
         add=[Card(value=1, status_effect="wound")]),
    Perk(description="Add one +0 Stun card",
         add=[Card(status_effect="stun")]),
    Perk(description="Add one +0 Add Target card",
         add=[Card(status_effect="target")])
]
beast_tyrant_perks = [
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Replace one -1 card with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Replace one -1 card with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Replace one -1 card with one +1 card",
         add=[Card(value=1)], remove=[-1]),
    Perk(description="Replace one +0 card with one +2 card",
         add=[Card(value=2)], remove=[0]),
    Perk(description="Replace one +0 card with one +2 card",
         add=[Card(value=2)], remove=[0]),
    Perk(description="Add one +1 Wound card",
         add=[Card(value=1, status_effect="wound")]),
    Perk(description="Add one +1 Wound card",
         add=[Card(value=1, status_effect="wound")]),
    Perk(description="Add one +1 Immobilize card",
         add=[Card(value=1, status_effect="immobilize")]),
    Perk(description="Add one +1 Immobilize card",
         add=[Card(value=1, status_effect="immobilize")]),
    Perk(description="Add two rolling Heal 1 cards",
         add=[Card(is_rolling=True, status_effect="heal_self1"),
              Card(is_rolling=True, status_effect="heal_self1")]),
    Perk(description="Add two rolling Heal 1 cards",
         add=[Card(is_rolling=True, status_effect="heal_self1"),
              Card(is_rolling=True, status_effect="heal_self1")]),
    Perk(description="Add two rolling Heal 1 cards",
         add=[Card(is_rolling=True, status_effect="heal_self1"),
              Card(is_rolling=True, status_effect="heal_self1")]),
    Perk(description="Add two rolling Earth cards",
         add=[Card(is_rolling=True, element="earth"),
              Card(is_rolling=True, element="earth")]),
    Perk(description="Ignore negative scenario effects")
]
diviner_perks = [
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove two -1 cards", remove=[-1, -1]),
    Perk(description="Remove one -2 card", remove=[-2]),
    Perk(description="Replace two +1 cards with one +3 Shield 1, Self card",
         add=[Card(value=3, status_effect="shield_self1")], remove=[1, 1]),
    Perk(description="Replace two +1 cards with one +3 Shield 1, Self card",
         add=[Card(value=3, status_effect="shield_self1")], remove=[1, 1]),
    Perk(description="Replace one +0 card with \
    one +1 Shield 1, Affect any Ally card",
         add=[Card(value=1, status_effect="shield_ally1")], remove=[0]),
    Perk(description="Replace one +0 card with one +2 Dark card",
         add=[Card(value=2, element="dark")], remove=[0]),
    Perk(description="Replace one +0 card with one +2 Light card",
         add=[Card(value=2, element="light")], remove=[0]),
    Perk(description="Replace one +0 card with one +3 Muddle card",
         add=[Card(value=3, status_effect="muddle")], remove=[0]),
    Perk(description="Replace one +0 card with one +3 Curse card",
         add=[Card(value=3, status_effect="curse")], remove=[0]),
    Perk(description="Replace one +0 card with one +2 Regenerate, Self card",
         add=[Card(value=2, status_effect="regenerate")], remove=[0]),
    Perk(description="Replace one -1 card with \
    one +1 Heal 2, Affect any Ally card",
         add=[Card(value=1, status_effect="heal_ally2")], remove=[-1]),
    Perk(description="Add two rolling Heal 1, Self cards",
         add=[Card(is_rolling=True, status_effect="heal_self1"),
              Card(is_rolling=True, status_effect="heal_self1")]),
    Perk(description="Add two rolling Curse cards",
         add=[Card(is_rolling=True, status_effect="curse"),
              Card(is_rolling=True, status_effect="curse")]),
    Perk(description="Ignore negative scenario effects and add two +1 cards",
         add=[Card(value=1), Card(value=1)])
]
class_dictionary = {
    'brute': brute_perks,
    'tinkerer': tinkerer_perks,
    'spellweaver': spellweaver_perks,
    'cragheart': cragheart_perks,
    'scoundrel': scoundrel_perks,
    'mindtheif': mindtheif_perks,
    'sunkeeper': sunkeeper_perks,
    'quartermaster': quartermaster_perks,
    'summoner': summoner_perks,
    'nightshroud': nightshroud_perks,
    'plagueherald': plagueherald_perks,
    'berserker': berserker_perks,
    'soothsinger': soothsinger_perks,
    'doomstalker': doomstalker_perks,
    'sawbones': sawbones_perks,
    'elementalist': elementalist_perks,
    'beast_tyrant': beast_tyrant_perks,
    'diviner': diviner_perks
}
