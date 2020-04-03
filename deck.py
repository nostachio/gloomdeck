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
        self.character_class = "none"
        self.status_effect = "none"
        self.element = "none"
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
        main = "images/blank.jpg"
        if self.value == "miss":
            main = "images/miss.png"
        if self.value == "-2":
            main = "images/minus_two.png"
        if self.value == "-1":
            main = "images/minus_one.png"
        if self.value == "0":
            main = "images/Neutral.png"
        if self.value == "1":
            main = "images/one.png"
        if self.value == "2":
            main = "images/two.png"
        if self.value == "2x":
            main = "images/2x.png"
        if self.value == "3":
            main = "images/blank.jpg"
        if self.value == "4":
            main = "images/blank.jpg"
        if self.value == "curse":
            main = "images/curse.png"
        if self.value == "bless":
            main = "images/bless.png"
        return main


class Character_Card(Card):
    """Cards added from perks."""

    def __init__(self, value, character_class, is_rolling, status_effect, element):
        """Initialize attributes."""
        self.value = value
        self.is_rolling = is_rolling
        self.character_class = character_class
        self.status_effect = status_effect
        self.element = element
        self.main_image = self.select_main_image()
        self.status_effect_image = self.select_status_effect_image(status_effect)
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
        self.character_class = "none"
        self.status_effect = "none"
        self.element = "none"
        self.main_image = self.select_main_image()


class Curse_Card(Card):
    """Curse Card."""

    def __init__(self):
        """Initialize attributes."""
        self.value = "curse"
        self.is_rolling = False
        self.character_class = "none"
        self.status_effect = "none"
        self.element = "none"
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
        for value in ["2x", 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -2, "miss"]:
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
        # if there isn't at least one card that is_rolling is false, continue pulling
        # discard all drawn cards
        # return selected cards
        pass

    def draw_with_disadvantage(self):
        """Draw cards with disadvantage."""
        # randomly select two Cards
        # if there isn't at least one card that is_rolling is false, continue pulling
        # discard all drawn cards
        # return selected cards
        pass

    def add_bless(self):
        """Add a bless card to the deck."""
        self.current_deck.append(Bless_Card())
        return
    # add method to remove bless
    # add method to remove curse

    def add_curse(self):
        """Add a curse card to the deck."""
        self.current_deck.append(Curse_Card())
        return

    def add_perk(self, perk):
        """Alter deck based on perk."""
        # add cards required to full_deck
        # remove cards required
        pass
