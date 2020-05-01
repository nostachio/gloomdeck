"""Perks class.

Define perks and their methods and data.
"""


class Perk:
    """Perks that alter decks."""

    def __init__(self, description="", add=[], remove=[], is_disabled=False):
        """Initialize attributes."""
        self.add_cards = []
        self.remove_cards = []
        self.description = description
        self.added = False
        self.is_disabled = is_disabled
        for card_attribute_set in add:
            self.add_cards.append(card_attribute_set)
        for card_attribute_set in remove:
            self.remove_cards.append(card_attribute_set)
        # print("perk")
        # print(self)
        # print(self.character_class)
        # print(self.add_cards)
        # print(self.remove_cards)
