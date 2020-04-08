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
