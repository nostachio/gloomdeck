"""Attack modifier deck tracker for Gloomhaven.

Lorem Ipsum.
"""
# import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.button import Button
import deck


class MainDeckScreen(FloatLayout):
    """Create the deck screen."""

    def draw(self):
        """Draw a single card."""
        drawn_card = myDeck.draw()
        print(deck.Card.get_value(drawn_card))

    def draw_with_advantage(self):
        """Draw cards with advantage."""
        print("draw with advantage")

    def draw_with_disadvantage(self):
        """Draw cards with disadvantage."""
        print("draw with disadvantage")

    def add_bless(self):
        """Add a bless card to the deck."""
        myDeck.add_bless()
        print("bless added")

    def add_curse(self):
        """Add a curse card to the deck."""
        myDeck.add_curse()
        print("curse added")


class DeckApp(App):
    """Make the main window."""

    def build(self):
        """Give deck screen to app."""
        return MainDeckScreen()


myDeck = deck.Deck("deck_name", "character_class")


if __name__ == '__main__':
    DeckApp().run()
