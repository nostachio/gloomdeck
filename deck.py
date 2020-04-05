"""Deck class.

Class for Decks.
"""
import random


class Card:
    """Attack modifier card with only a numeric value or miss or double."""

    def __init__(self, value):
        """Initialize attributes."""
        self.value = str(value)
        self.is_rolling = False
        self.character_class = None
        self.status_effect = None
        self.element = None
        self.main_image = self.select_main_image()

    def get_value(self):
        """Return string of value."""
        return self.value

    def get_is_rolling(self):
        """Return boolean of is_rolling."""
        return self.is_rolling

    def get_status_effect(self):
        """Return string of status_effect."""
        return self.status_effect

    def select_main_image(self):
        """Add corresponding image to card."""
        main_image = "images/{0}.png".format(self.value)
        return main_image

    def is_this_card_better_than_me(self, card_to_compare):
        """Return if the card is better, worse, or similar."""
        am_i_better = None
        if self.value == "miss" or self.value == "curse":
            am_i_better = False
        elif card_to_compare.value == "miss" or\
                card_to_compare.value == "curse":
            am_i_better = True
        else:
            if self.value < card_to_compare.value:
                am_i_better = False
            elif self.value == card_to_compare.value:
                # compare status
                if self.status_effect is None and\
                        card_to_compare.status_effect is not None:
                    am_i_better = False
                elif self.status_effect is not None and\
                        card_to_compare.status_effect is not None:
                    # then compare elements
                    if self.element is None and\
                            card_to_compare.element is not None:
                        am_i_better = False
                    elif self.element is not None\
                            and card_to_compare.element is None:
                        am_i_better = True
                    else:
                        # make this player's choice
                        am_i_better = None
                else:
                    am_i_better = True
            else:
                am_i_better = True
        return am_i_better


class Character_Card(Card):
    """Cards added from perks."""

    def __init__(self, value, character_class,
                 is_rolling, status_effect, element):
        """Initialize attributes."""
        self.value = value
        self.is_rolling = is_rolling
        self.character_class = character_class
        self.status_effect = status_effect
        self.element = element
        self.main_image = self.select_main_image()
        self.status_effect_image = self.select_status_effect_image(
            status_effect)
        self.element_image = self.select_element_image(element)

    def select_status_effect_image(status_effect):
        """Pick image for status effect."""
        if status_effect == "stun":
            image = "images/"
        if status_effect == "immobilize":
            image = "images/"
        if status_effect == "disarm":
            image = "images/"
        if status_effect == "wound":
            image = "images/"
        if status_effect == "muddle":
            image = "images/"
        if status_effect == "poison":
            image = "images/"
        if status_effect == "strengthen":
            image = "images/"
        if status_effect == "invisible":
            image = "images/"
        if status_effect == "regenerate":
            image = "images/"
        return image

    def select_element_image(element):
        """Get the image for the element effect."""
        if element == "air":
            image = "images/"
        if element == "earth":
            image = "images/"
        if element == "fire":
            image = "images/"
        if element == "water":
            image = "images/"
        if element == "light":
            image = "images/"
        if element == "dark":
            image = "images/"
        if element == "any":
            image = "images/"
        return image


class Bless_Card(Card):
    """Bless Card."""

    def __init__(self):
        """Initialize attributes."""
        self.value = "bless"
        self.is_rolling = False
        self.character_class = None
        self.status_effect = None
        self.element = None
        self.main_image = self.select_main_image()


class Curse_Card(Card):
    """Curse Card."""

    def __init__(self):
        """Initialize attributes."""
        self.value = "curse"
        self.is_rolling = False
        self.character_class = None
        self.status_effect = None
        self.element = None
        self.main_image = self.select_main_image()


class Perk:
    """Perks that alter decks."""

    def __init__(self, add_cards, remove_cards):
        """Initialize attributes."""
        pass


class Deck:
    """A deck that can be modified."""

    def __init__(self, name, character_class):
        """Initialize attributes."""
        self.name = name
        self.full_deck = []
        for value in ["2x", 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1, -1, -1,
                      -1, -1, -2, "miss"]:
            self.full_deck.append(Card(value))
        self.current_deck = self.full_deck
        self.discard = []
        self.active_perks = []
        self.available_perks = []

    def shuffle(self):
        """Shuffle deck."""
        for card in self.discard:
            if card.value == "bless" or card.value == "curse":
                self.discard.remove(card)
        self.current_deck = self.current_deck + self.discard
        self.discard = []
        return

    def draw(self):
        """Draw a card normally."""
        if len(self.current_deck) == 0:
            self.shuffle()
        choice = random.choice(self.current_deck)
        self.current_deck.remove(choice)
        self.discard.append(choice)
        return choice

    def draw_with_advantage(self):
        """Draw cards with advantage."""
        # randomly select two Cards
        card_list = []
        rolling_modifiers = []
        is_better = None
        while len(card_list) < 1 or\
                (len(card_list) + len(rolling_modifiers) < 2):
            this_card = self.draw()
            if not this_card.get_is_rolling():
                card_list.append(this_card)
            else:
                rolling_modifiers.append(this_card)
        if len(card_list) == 1:
            is_better = True
        if len(card_list) == 2:
            is_better = card_list[0].is_this_card_better_than_me(card_list[1])
        return_list = [card_list, is_better, rolling_modifiers]
        return return_list

    def draw_with_disadvantage(self):
        """Draw cards with disadvantage."""
        card_list = []
        pull_discard = []
        is_better = None
        while (len(card_list) + len(pull_discard) < 2) or len(card_list) < 1:
            this_card = self.draw()
            if not this_card.get_is_rolling():
                card_list.append(this_card)
            else:
                pull_discard.append(this_card)
        if len(card_list) == 1:
            is_better = True
        if len(card_list) == 2:
            is_better = card_list[0].is_this_card_better_than_me(card_list[1])
        return_list = [card_list, is_better, pull_discard]
        return return_list

    def add_bless(self):
        """Add a bless card to the deck."""
        self.current_deck.append(Bless_Card())
        return

    def remove_bless(self):
        """Remove a bless card from the deck."""
        pass

    def add_curse(self):
        """Add a curse card to the deck."""
        self.current_deck.append(Curse_Card())
        return

    def remove_curse(self):
        """Remove a curse card from the deck."""
        pass

    def add_perk(self, perk):
        """Alter deck based on perk."""
        # add cards required to full_deck
        # remove cards required
        pass

    def needs_shuffling(self):
        """Check for a miss or 2x in discard pile."""
        for card in self.discard:
            if card.value == "miss" or "2x":
                return True

    def save_deck(self):
        """Save deck to somewhere based on name."""
        pass
