"""Perks class.

Define perks and their methods and data.
"""


class Perk:
    """Perks that alter decks."""

    def __init__(self, character_class, add_cards, remove_cards):
        """Initialize attributes."""
        self.character_class = character_class
        self.add_cards = []
        self.remove_cards = []
        for card in add_cards:
            self.add_cards.append(card)
        for card in remove_cards:
            self.remove_cards.append(card)
        print("perk")
        print(self)
        print(self.character_class)
        print(self.add_cards)
        print(self.remove_cards)
