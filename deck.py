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
        self.cards = []
        for card in cards:
            self.cards.append(card)
        self.modifiers = []
        for modifier in modifiers:
            self.modifiers.append(modifier)
        self.attack = self.attack_result()
        self.status_effects = self.status_effect_result()
        self.elements = self.elements_result()

    def attack_result(self):
        """Add up the attack modifiers."""
        attack_values = []
        attack_multiplier = 1
        attack_sum = 0
        no_damage = False
        if self.draw_type == "simple" or (self.draw_type == "advantage"
                                          and len(self.cards == 1)):
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
            if value == "2x" or card.value == "bless":
                attack_multiplier = 2
            elif value == "miss" or card.value == "curse":
                no_damage = True
            else:
                attack_sum += value
        total_attack = attack_sum * attack_multiplier
        if no_damage:
            total_attack = "no_damage"
        return total_attack

    def status_effect_result(self):
        """Combine all status effects."""
        status_effect_list = []
        self.status_effects = {
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
            'pull1': 0,
            'pierce3': 0,
            'target': 0,
            'heal_self1': 0,
            'heal_self2': 0,
            'heal_self3': 0,
            'heal_ally2': 0,
            'shield_self1': 0,
            'shield_ally1': 0,
            'curse': 0,
            'item': False
        }
        if self.draw_type == "simple" or (self.draw_type == "advantage"
                                          and len(self.cards == 1)):
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
            if card.status_effect in ['push', 'pull', 'pierce', 'target',
                                      'heal_self', 'heal_ally',
                                      'shield_self', 'shield_ally',
                                      'curse']:
                self.status_effect['{0}'.format(effect)] += 1
            elif card.status_effect is not None:
                self.status_effects['{0}'.format(effect)] = True

    def elements_result(self):
        """Define result of last draw."""
        element_list = []
        self.elements = {
            'light': False,
            'dark': False,
            'fire': False,
            'ice': False,
            'earth': False,
            'wind': False
        }
        if self.draw_type == "simple" or (self.draw_type == "advantage"
                                          and len(self.cards == 1)):
            for card in (self.cards + self.modifiers):
                element_list.append(card.status_effect)
        elif self.draw_type == "advantage":
            # append better card.  no modifiers will be present
            card_set = self.cards[0].card_comparison(self.cards[1])
            element_list.append(card_set['better_card'].element)
        else:  # disadvantage
            if len(self.cards) == 2:
                card_set = self.cards[0].card_comparison(self.cards[1])
                element_list.append(card_set['worse_card'].element)
            else:
                element_list.append(self.cards[0].element)
        for element in element_list:
            if element is not None:
                self.elements['{0}'.format(element)] = True


class Deck:
    """A deck that can be modified."""

    def __init__(self, name, character_class):
        """Initialize attributes."""
        self.name = name
        self.character_class = characters.Character_Class(character_class)
        self.full_deck = []
        for value in ["2x", 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1, -1, -1,
                      -1, -1, -2, "miss"]:
            self.full_deck.append(cards.Card(value))
        self.current_deck = self.full_deck
        self.discard = []
        self.active_perks = []
        self.available_perks = self.character_class.perks
        self.bless_count = self.count_blesses()
        self.curse_count = self.count_curses()
        # will figure out what to call extra -1 cards later
        self.demerit = 0
        # last_draw will be [type_of_draw, [cards], [modifiers]]
        self.last_draw = None
        self.add_all_perks()

    def shuffle(self):
        """Shuffle deck."""
        for card in self.discard:
            if card.value == "bless" or card.value == "curse":
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
            if choice.is_rolling:
                modifiers.append(choice)
            else:
                cards.append(choice)
            self.current_deck.remove(choice)
            self.discard.append(choice)
        self.last_draw = Last_Draw(type_of_draw, cards, modifiers)

    def add_bless(self):
        """Add a bless card to the deck."""
        self.current_deck.append(cards.Bless_Card())
        return

    def remove_bless(self):
        """Remove a bless card from the deck."""
        pass

    def count_blesses(self):
        """Count the number of bless cards in the deck."""
        return sum(1 for card in self.current_deck if card.value == "bless")

    def add_curse(self):
        """Add a curse card to the deck."""
        self.current_deck.append(cards.Curse_Card())
        return

    def remove_curse(self):
        """Remove a curse card from the deck."""
        pass

    def count_curses(self):
        """Count the number of curse cards in the deck."""
        return sum(1 for card in self.current_deck if card.value == "curse")

    def add_all_perks(self):
        """Temporary method to add all perks to deck for testing."""
        for perk in self.available_perks:
            self.add_perk(perk)

    def add_perk(self, perk):
        """Alter deck based on perk."""
        # add cards required to full_deck
        # remove cards required
        for card in perk.add_cards:
            self.full_deck.append(card)
        for value in perk.remove_cards:
            for index, card in enumerate(self.full_deck):
                if card.element is None and card.status_effect is None:
                    if str(card.value) == str(value):
                        self.full_deck.pop(index)
                        break

    def needs_shuffling(self):
        """Check for a miss or 2x in discard pile."""
        for card in self.discard:
            if card.value == "miss" or "2x":
                return True

    def save_deck(self):
        """Save deck to somewhere based on name."""
        pass
