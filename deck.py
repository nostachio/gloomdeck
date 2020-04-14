"""Deck class.

Class for Decks.
"""
import random
import cards
import characters


class Last_Draw:
    """Holds the cards for a draw."""

    def __init__(self, draw_type, cards, modifiers):
        """Initialize attributes."""
        self.draw_type = draw_type
        self.double_damage = False
        self.no_damage = False
        self.cards = []
        for card in cards:
            self.cards.append(card)
        self.modifiers = []
        for modifier in modifiers:
            self.modifiers.append(modifier)
        self.attack = self.attack_result()
        self.status_effects = self.status_effect_result()
        self.elements = self.elements_result()
        # print(self.status_effects)

    def attack_result(self):
        """Add up the attack modifiers."""
        attack_values = []
        attack_sum = 0
        if self.draw_type == "simple" or (self.draw_type == "advantage"
                                          and len(self.cards) == 1):
            for card in (self.cards + self.modifiers):
                attack_values.append(card.value)
        elif self.draw_type == "advantage":
            # append better card.  no modifiers will be present
            card_set = self.cards[0].card_comparison(self.cards[1])
            attack_values.append(card_set['better_card'].value)
        else:  # disadvantage
            if len(self.cards) == 2:
                card_set = self.cards[0].card_comparison(self.cards[1])
                attack_values.append(card_set['worse_card'].value)
            else:
                attack_values.append(self.cards[0].value)
        for value in attack_values:
            if value == "2x" or value == "bless":
                self.double_damage = True
            elif value == "miss" or value == "curse":
                self.no_damage = True
            else:
                attack_sum += int(value)
        total_attack = attack_sum
        return total_attack

    def status_effect_result(self):
        """Combine all status effects."""
        status_effect_list = []
        status_effects = {
            'stun': False,
            'immobilize': False,
            'disarm': False,
            'wound': False,
            'muddle': False,
            'poison': False,
            'strengthen': False,
            'invisible': False,
            'regenerate': False,
            'push1': 0,
            'push2': 0,
            'push_total': 0,
            'pull1': 0,
            'pull_total': 0,
            'pierce3': 0,
            'pierce_total': 0,
            'target': 0,
            'target_total': 0,
            'heal_self1': 0,
            'heal_self2': 0,
            'heal_self3': 0,
            'heal_self_total': 0,
            'heal_ally2': 0,
            'heal_ally_total': 0,
            'shield_self1': 0,
            'shield_self_total': 0,
            'shield_ally1': 0,
            'shield_ally_total': 0,
            'curse': 0,
            'item': False
        }
        if self.draw_type == "simple" or (self.draw_type == "advantage"
                                          and len(self.cards) == 1):
            for card in (self.cards + self.modifiers):
                status_effect_list.append(card.status_effect)
        elif self.draw_type == "advantage":
            # append better card.  no modifiers will be present
            card_set = self.cards[0].card_comparison(self.cards[1])
            status_effect_list.append(card_set['better_card'].status_effect)
        else:  # disadvantage
            if len(self.cards) == 2:
                card_set = self.cards[0].card_comparison(self.cards[1])
                status_effect_list.append(card_set['worse_card'].status_effect)
            else:
                status_effect_list.append(self.cards[0].status_effect)
        for effect in status_effect_list:
            if effect in ['push1', 'push2', 'pull1', 'pierce3', 'target',
                          'heal_self1', 'heal_self2', 'heal_self3',
                          'heal_ally2', 'shield_self1', 'shield_ally1',
                          'curse']:
                status_effects['{0}'.format(effect)] += 1
            else:
                status_effects['{0}'.format(effect)] = True
        status_effects['push_total'] =\
            ((1 * status_effects['push1'])
             + (2 * status_effects['push2']))
        status_effects['pull_total'] =\
            (1 * status_effects['pull1'])
        status_effects['pierce_total'] =\
            (3 * status_effects['pierce3'])
        status_effects['target_total'] =\
            (1 * status_effects['target'])
        status_effects['heal_self_total'] = (
            (1 * status_effects['heal_self1'])
            + (2 * status_effects['heal_self2'])
            + (3 * status_effects['heal_self3']))
        status_effects['heal_ally_total'] =\
            (2 * status_effects['heal_ally2'])
        status_effects['shield_self_total'] =\
            (1 * status_effects['shield_self1'])
        status_effects['shield_ally_total'] =\
            (1 * status_effects['shield_ally1'])
        status_effects.pop('None', None)
        return status_effects

    def elements_result(self):
        """Define result of last draw."""
        elements = {
            'light': False,
            'dark': False,
            'fire': False,
            'ice': False,
            'earth': False,
            'wind': False
        }
        if self.draw_type == "simple" or (self.draw_type == "advantage"
                                          and len(self.cards) == 1):
            for card in (self.cards + self.modifiers):
                elements[card.element] = True
        elif self.draw_type == "advantage":
            # append better card.  no modifiers will be present
            card_set = self.cards[0].card_comparison(self.cards[1])
            elements[card_set['better_card'].element] = True
        else:  # disadvantage
            if len(self.cards) == 2:
                card_set = self.cards[0].card_comparison(self.cards[1])
                elements[card_set['worse_card'].element] = True
            else:
                elements[self.cards[0].element] = True
        elements.pop(None, None)
        return elements


class Deck:
    """A deck that can be modified."""

    def __init__(self, name, character_class):
        """Initialize attributes."""
        self.name = name
        self.character_class = characters.Character_Class(character_class)
        self.full_deck = []
        self.standard_deck = []
        for value in ["2x", 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1, -1, -1,
                      -1, -1, -2, "miss"]:
            self.standard_deck.append(cards.Card(value=value))
        self.current_deck = self.standard_deck
        self.discard = []
        self.active_perks = []
        self.available_perks = self.character_class.perks
        self.bless_count = 0
        self.curse_count = 0
        # will figure out what to call extra -1 cards later
        self.demerit = 0
        self.demerit_count = 0
        # last_draw will be [type_of_draw, [cards], [modifiers]]
        self.last_draw = None
        self.add_all_perks()

    def shuffle(self):
        """Shuffle deck."""
        for card in self.discard:
            if card.type == "bless" or card.type == "curse":
                self.discard.remove(card)
        self.current_deck = self.current_deck + self.discard
        self.discard = []
        return

    def draw(self, type_of_draw):
        """Draw a card normally."""
        cards = []
        modifiers = []
        if type_of_draw == "simple":
            minimum_cards = 1
        else:
            minimum_cards = 2
        while len(cards) == 0 or\
                (len(cards) + len(modifiers)) < minimum_cards:
            if len(self.current_deck) == 0:
                self.shuffle()
            choice = random.choice(self.current_deck)
            print(choice.__dict__)
            if choice.is_rolling:
                modifiers.append(choice)
            else:
                cards.append(choice)
            self.current_deck.remove(choice)
            self.discard.append(choice)
        self.last_draw = Last_Draw(type_of_draw, cards, modifiers)

    def add_bless(self):
        """Add a bless card to the deck."""
        self.current_deck.append(cards.Card("bless", type="bless"))
        return

    def remove_bless(self):
        """Remove a bless card from the deck."""
        pass

    def count_blesses(self):
        """Count the number of bless cards in the deck."""
        return sum(1 for card in self.current_deck if card.type == "bless")

    def add_curse(self):
        """Add a curse card to the deck."""
        self.current_deck.append(cards.Card("curse", type="curse"))
        return

    def remove_curse(self):
        """Remove a curse card from the deck."""
        pass

    def count_curses(self):
        """Count the number of curse cards in the deck."""
        return sum(1 for card in self.current_deck if card.type == "curse")

    def add_demerit(self):
        """Add a demerit card to the deck."""
        self.current_deck.append(cards.Card(-1, type="demerit"))
        return

    def remove_demerit(self):
        """Remove a demerit card from the deck."""
        pass

    def count_demerits(self):
        """Count the number of bless cards in the deck."""
        return sum(1 for card in (self.current_deck + self.discard)
                   if card.type == "demerit")

    def add_all_perks(self):
        """Temporary method to add all perks to deck for testing."""
        for perk in self.available_perks:
            self.add_perk(perk)

    def add_perk(self, perk):
        """Alter deck based on perk."""
        # add cards required to full_deck
        # remove cards required
        for card in perk.add_cards:
            card.character_class = self.character_class.character_class
            # print(self.character_class)
            # print(card.character_class)
            card.type = 'perk'
            print(card.type)
            card.derive_images()
            self.current_deck.append(card)
        for value in perk.remove_cards:
            if value == "nightshroud_minus_one_dark":
                pass
                # add in the eclipse exception
                # not sure we want to pull from full_deck
            for index, card in enumerate(self.current_deck):
                if card.type == "None":
                    if str(card.value) == str(value):
                        self.current_deck.pop(index)
                        break

    def needs_shuffling(self):
        """Check for a miss or 2x in discard pile."""
        for card in self.discard:
            if card.value == "miss" or "2x":
                return True

    def save_deck(self):
        """Save deck to somewhere based on name."""
        pass
