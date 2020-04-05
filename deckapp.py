"""Attack modifier deck tracker for Gloomhaven.

Lorem Ipsum.
"""
# import kivy
from kivy.app import App
# from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
# from kivy.uix.button import Button
from kivy.uix.image import Image
import deck
from kivy.core.window import Window
Window.size = (360, 780)


class MainDeckScreen(RelativeLayout):
    """Create the deck screen."""

    def draw(self):
        """Draw a single card."""
        for item in self.children[-1].children:
            if isinstance(item, RelativeLayout):
                item.clear_widgets()
        # for item in self.children[0].children:
        #     if isinstance(item, RelativeLayout):
        #         while len(item.children) > 0:
        #             for subitem in item.children:
        #                 item.remove_widget(subitem)
        #                 print(item.children)
        #                 print(subitem)
        drawn_card = myDeck.draw()
        print(deck.Card.get_value(drawn_card))
        self.ids.discard_main.source =\
            "images/{0}.png".format(drawn_card.value)
        self.update_discard()

    def draw_with_advantage(self):
        """Draw cards with advantage."""
        card_list, is_better, rolling_modifiers = myDeck.draw_with_advantage()
        if len(card_list) == 2:
            disad2_value = card_list[1].value
        else:
            disad2_value = rolling_modifiers[0].value
        # self.ids.disad1_main.source =\
        #     "images/{0}.png".format(card_list[0].value)
        # if len(card_list) == 2:
        #     self.ids.disad2_main.source = \
        #         "images/{0}.png".format(card_list[1].value)
        # else:
        #     self.ids.disad2_main.source = \
        #         "images/{0}.png".format(rolling_modifiers[0].value)
        disad_layout =\
            RelativeLayout(id=("disad_layout"),
                           size_hint_y=(0.3),
                           size_hint_x=(1),
                           pos_hint=({'center_x': 0.5, 'center_y': 0.35}))
        disad1 = Image(source=('images/blank.jpg'),
                       size_hint_x=(0.55),
                       size_hint_y=(0.55),
                       pos_hint=({'center_x': 0.3, 'center_y': 0.3}),
                       allow_stretch=(True))
        disad1_mod =\
            Image(source=('images/{0}.png'.format(card_list[0].value)),
                  size_hint_x=(0.55),
                  size_hint_y=(0.55),
                  pos_hint=({'center_x': 0.3, 'center_y': 0.3}),
                  allow_stretch=(True))
        disad2 = Image(source=('images/blank.jpg'),
                       size_hint_x=(0.55),
                       size_hint_y=(0.55),
                       pos_hint=({'center_x': 0.7, 'center_y': 0.7}),
                       allow_stretch=(True))
        disad2_mod = Image(source=('images/{0}.png'.format(disad2_value)),
                           size_hint_x=(0.55),
                           size_hint_y=(0.55),
                           pos_hint=({'center_x': 0.7, 'center_y': 0.7}),
                           allow_stretch=(True))
        for item in self.children[0].children:
            if isinstance(item, RelativeLayout):
                self.children[0].clear_widgets(item)
        self.children[0].add_widget(disad_layout)
        for item in self.children[-1].children:
            if isinstance(item, RelativeLayout):
                item.add_widget(disad2)
                item.add_widget(disad2_mod)
                item.add_widget(disad1)
                item.add_widget(disad1_mod)
        self.update_discard()

    def draw_with_disadvantage(self):
        """Draw cards with disadvantage."""
        card_list, is_better, pull_discard = myDeck.draw_with_disadvantage()
        if len(card_list) == 2:
            disad2_value = card_list[1].value
        else:
            disad2_value = pull_discard[0].value
        disad_layout =\
            RelativeLayout(id=("disad_layout"),
                           size_hint_y=(0.3),
                           size_hint_x=(1),
                           pos_hint=({'center_x': 0.5, 'center_y': 0.35}))
        disad1 = Image(source=('images/blank.jpg'),
                       size_hint_x=(0.55),
                       size_hint_y=(0.55),
                       pos_hint=({'center_x': 0.3, 'center_y': 0.3}),
                       allow_stretch=(True))
        disad1_mod =\
            Image(source=('images/{0}.png'.format(card_list[0].value)),
                  size_hint_x=(0.55),
                  size_hint_y=(0.55),
                  pos_hint=({'center_x': 0.3, 'center_y': 0.3}),
                  allow_stretch=(True))
        disad2 = Image(source=('images/blank.jpg'),
                       size_hint_x=(0.55),
                       size_hint_y=(0.55),
                       pos_hint=({'center_x': 0.7, 'center_y': 0.7}),
                       allow_stretch=(True))
        disad2_mod = Image(source=('images/{0}.png'.format(disad2_value)),
                           size_hint_x=(0.55),
                           size_hint_y=(0.55),
                           pos_hint=({'center_x': 0.7, 'center_y': 0.7}),
                           allow_stretch=(True))
        # self.ids.disad1_main.source =\
        #     "images/{0}.png".format(card_list[0].value)
        # if len(card_list) == 2:
        #     self.ids.disad2_main.source = \
        #         "images/{0}.png".format(card_list[1].value)
        # else:
        #     self.ids.disad2_main.source = \
        #         "images/{0}.png".format(pull_discard[0].value)
        # for item in self.children[0].children:
        #     print("self.children", self.children)
        #     print("self.parent.children", self.parent.children)
        #     print("self.children[0].children", self.children[0].children)
        #     print("self.children[0].children", self.children[0].children)
        #     if isinstance(item, RelativeLayout):
        #         print("RelativeLayout children", item.children)
        #         for subitem in self.children[0].children:
        #             item.remove_widget(subitem)
        #         # item.clear_widgets()
        for item in self.children[0].children:
            if isinstance(item, RelativeLayout):
                self.children[0].clear_widgets(item)
        self.children[0].add_widget(disad_layout)
        for item in self.children[-1].children:
            if isinstance(item, RelativeLayout):
                item.add_widget(disad2)
                item.add_widget(disad2_mod)
                item.add_widget(disad1)
                item.add_widget(disad1_mod)
        self.update_discard()

    def add_bless(self):
        """Add a bless card to the deck."""
        myDeck.add_bless()
        print("bless added")

    def add_curse(self):
        """Add a curse card to the deck."""
        myDeck.add_curse()
        print("curse added")

    def update_discard(self):
        """Display the last x cards in discard."""
        while len(self.children) > 1:
            for item in self.children:
                if isinstance(item, Image):
                    self.remove_widget(item)
        for i, card in enumerate(reversed(myDeck.discard)):
            # make image with blank
            cx = (0.1 + (0.1 * (i % 9)))
            cy = 0.15 - (.05 * (i / 9))
            base_card = Image(size_hint_x=(0.1), size_hint_y=(0.1),
                              source=('images/blank.jpg'),
                              allow_stretch=(True),
                              id=('discard_base'),
                              pos_hint=({'center_y': cy, 'center_x': cx}))
            modifier = Image(size_hint_x=(0.1),
                             size_hint_y=(0.1),
                             id=('discard_mod'),
                             source=('images/{}.png'.format(card.value)),
                             allow_stretch=(True),
                             pos_hint=({'center_y': cy, 'center_x': cx}))
            self.add_widget(base_card)
            self.add_widget(modifier)

    def shuffle(self):
        """Shuffle the deck."""
        myDeck.shuffle()
        self.update_discard()


class DeckApp(App):
    """Make the main window."""

    def build(self):
        """Give deck screen to app."""
        return MainDeckScreen()


myDeck = deck.Deck("deck_name", "character_class")


if __name__ == '__main__':
    DeckApp().run()
