"""Attack modifier deck tracker for Gloomhaven.

Lorem Ipsum.
"""
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
import deck
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import DictProperty
# from kivy.properties import ListProperty
from kivy.core.window import Window
Window.size = (360, 780)


class MainDeckScreen(RelativeLayout):
    """Create the deck screen."""


class TopButtons(RelativeLayout):
    """Place for the curse, shuffle, bless buttons."""

    def update(self):
        """Update all top buttons."""
        CurseButton.update(self.children[2])
        DemeritButton.update(self.children[3])
        BlessButton.update(self.children[4])
        ShuffleButton.update(self.children[5])


class DrawButton(Button):
    """Class for anything that causes a draw action."""

    def draw(self, type_of_draw):
        """Draw cards."""
        myDeck.draw(type_of_draw)
        Discard.update(self.parent.parent.children[1])
        DiscardHistory.update_discard(self.parent.parent.children[0])
        DrawResult.update(self.parent.parent.children[2])
        TopButtons.update(self.parent.parent.children[3])


class DisadvantageButton(DrawButton):
    """Disadvantage Button Widget."""

    pass


class AdvantageButton(DrawButton):
    """Advantage Button Widget."""

    pass


class BlessButton(Button):
    """Class for bless button."""

    def update(self):
        """Change the label number to number of blesses in deck."""
        self.text = str(myDeck.count_blesses())

    def add_bless(self):
        """Add a bless card to the deck."""
        myDeck.add_bless()
        self.update()
        print("bless added")


class CurseButton(Button):
    """Class for curse button."""

    def update(self):
        """Change the label number to number of curses in deck."""
        self.text = str(myDeck.count_curses())

    def add_curse(self):
        """Add a curse card to the deck."""
        myDeck.add_curse()
        self.update()
        print("curse added")


class DemeritButton(Button):
    """Class for demerit button."""

    def update(self):
        """Change the label number to number of curses in deck."""
        self.text = str(myDeck.count_demerits())

    def add_demerit(self):
        """Add a demerit card to the deck."""
        myDeck.add_demerit()
        self.update()
        print("demerit added")


class Deck(RelativeLayout):
    """Deck widget."""


class ShuffleButton(Button):
    """Shuffle Button Widget."""

    def update(self):
        """Determine if shuffle is available."""
        for card in myDeck.discard:
            if card.value == "2x" or card.value == "miss":
                self.disabled = True
        else:
            self.disabled = False

    def shuffle(self):
        """Shuffle the deck."""
        myDeck.shuffle()
        DiscardHistory.update_discard(self.parent.parent.children[0])
        TopButtons.update(self.parent.parent.children[3])


class DiscardHistory(RelativeLayout):
    """Discard pile widget."""

    def update_discard(self):
        """Display the last x cards in discard."""
        self.clear_widgets()
        for i, this_card in enumerate(reversed(myDeck.discard)):
            # print("length", len(myDeck.discard))
            # print("discard", myDeck.discard)
            # print(this_card)
            # print("i", i)
            cx = (0.1 + (0.1 * (i % 9)))
            cy = 0.95 - (.25 * (i / 9))
            # print("forforfor")
            # print("prewidget")
            this_card_widget = SpecificCard(
                modifier_image=this_card.main_image,
                element_image=this_card.element_image,
                status_image=this_card.status_effect_image,
                rolling_image=this_card.rolling_image,
                class_image=this_card.character_class_image,
                allow_stretch=True,
                size_hint_x=(.1),
                size_hint_y=(.3),
                pos_hint=({'center_y': cy, 'center_x': cx})
            )
            # print("postwidget, pre-add-widget")
            self.add_widget(this_card_widget)
            # print("postaddwidget")
            # base_card = Image(size_hint_x=(0.1), size_hint_y=(0.3),
            #                   source=('images/blank.jpg'),
            #                   allow_stretch=(True),
            #                   id=('discard_base'),
            #                   pos_hint=({'center_y': cy, 'center_x': cx}))
            # modifier = Image(size_hint_x=(0.1),
            #                  size_hint_y=(0.3),
            #                  id=('discard_mod'),
            #                  source=(this_card.main_image),
            #                  allow_stretch=(True),
            #                  pos_hint=({'center_y': cy, 'center_x': cx}))
            # self.add_widget(base_card)
            # self.add_widget(modifier)
            # if this_card.is_rolling:
            #     rolling = SpecificCard(
            #         modifier_image=this_card.main_image,
            #         element_image=this_card.element_image,
            #         status_image=this_card.status_effect_image,
            #         rolling_image=this_card.rolling_image,
            #         class_image=this_card.character_class_image,
            #         allow_stretch=True,
            #         size_hint_x=(.1),
            #         size_hint_y=(.3),
            #         pos_hint=({'center_y': cy, 'center_x': cx})
            #     )
            #     self.add_widget(rolling)


# class SpecificCard(RelativeLayout):
class SpecificCard(RelativeLayout):
    """Card Widget."""

    modifier_image = StringProperty('images/null.png')
    status_image = StringProperty('images/null.png')
    element_image = StringProperty('images/null.png')
    rolling_image = StringProperty('images/null.png')
    class_image = StringProperty('images/null.png')
    my_size_hint_x = NumericProperty(1)
    my_size_hint_y = NumericProperty(1)
    my_pos_hint = DictProperty({'center_x': 0.5, 'center_y': 0.5})
    my_opacity = NumericProperty(1)


class DrawResult(GridLayout):
    """Draw result display widget."""

    #
    # my_columns = NumericProperty(2)

    def update(self):
        """Display results of draw."""
        count_status_icons = {
            'push_total': 'images/push.png',
            'pull_total': 'images/pull.png',
            'pierce_total': 'images/pierce.png',
            'target_total': 'images/target.png',
            'heal_self_total': 'images/heal_white.png',
            'heal_ally_total': 'images/heal_white.png',
            'shield_self_total': 'images/shield_white.png',
            'shield_ally_total': 'images/shield_white.png',
            'curse': 'images/curse.png'
        }
        self.clear_widgets()
        # widgets = []
        # number
        card = Image(source=('images/ability_card.png'))
        attack_icon = Image(
            source=('images/attack_white.png')
        )
        multiplier = Label(text='*')
        if myDeck.last_draw.no_damage:
            # miss icon widget
            attack = Image(
                source=('images/miss.png')
            )
            self.add_widget(attack)
        elif myDeck.last_draw.double_damage:
            print(myDeck.last_draw.no_damage)
            double = Image(
                source=('images/2x.png')
            )
            attack = Label(
                text=(str(myDeck.last_draw.attack))
            )
            add = Label(text='+')
            open = Label(text='(')
            close = Label(text=')')
            self.add_widget(open)
            self.add_widget(card)
            self.add_widget(add)
            self.add_widget(attack)
            self.add_widget(close)
            self.add_widget(multiplier)
            self.add_widget(double)
            self.add_widget(attack_icon)
        else:
            # label with myDeck.last_draw.attack
            attack = Label(
                text=(str(myDeck.last_draw.attack))
            )
            if myDeck.last_draw.attack >= 0:
                add = Label(text='+')
            else:
                add = Label(text='')
            self.add_widget(card)
            self.add_widget(add)
            self.add_widget(attack)
            # attack icon
            self.add_widget(attack_icon)
        # element icons
        # print(myDeck.last_draw.elements)
        for key in myDeck.last_draw.elements:
            if myDeck.last_draw.elements[key]:
                # print("key", key)
                # print("myDeck.last_draw.elements[key]",
                #       myDeck.last_draw.elements[key])
                element_widget = Image(
                    source=('images/{0}.png'.format(key)),
                    allow_stretch=(True)
                )
                self.add_widget(element_widget)
        # status icons
        for status in myDeck.last_draw.status_effects:
            if status in ['push_total', 'pull_total', 'pierce_total',
                          'target_total', 'heal_self_total', 'heal_ally_total',
                          'shield_self_total', 'shield_ally_total', 'curse']:
                if myDeck.last_draw.status_effects[status] > 0:
                    print(myDeck.last_draw.status_effects[status])
                    text = str(myDeck.last_draw.status_effects[status])
                    number = Label(text=(text))
                    numbered_status = Image(
                        source=(count_status_icons['{0}'.format(status)])
                    )
                    self.add_widget(number)
                    self.add_widget(numbered_status)
            elif status in ['push1', 'push2', 'pull1', 'pierce3', 'target',
                            'heal_self1', 'heal_self2', 'heal_self3',
                            'heal_ally2', 'shield_self1', 'shield_ally1']:
                pass
            elif myDeck.last_draw.status_effects[status]:
                status_widget = Image(
                    source=('images/{0}.png'.format(status)))
                self.add_widget(status_widget)
        # self.my_columns = len(widgets)
        # for widget in widgets:
        #     self.add_widget(widget)


class Discard(RelativeLayout):
    # class Discard(SpecificCard):
    """Discard Pile Widget."""

    # my_size_hint_x = NumericProperty(1)
    # my_size_hint_y = NumericProperty(0.3)
    # my_pos_hint = DictProperty({'center_x': 0.5, 'center_y': 0.35})

    def update(self):
        """Place cards onto discard pile."""
        self.clear_widgets()
        if myDeck.last_draw.draw_type == "simple":
            main_card = myDeck.last_draw.cards[0]
            discard = SpecificCard(
                modifier_image=main_card.main_image,
                element_image=main_card.element_image,
                status_image=main_card.status_effect_image,
                rolling_image=main_card.rolling_image,
                class_image=main_card.character_class_image,
                my_pos_hint=({'center_x': 0.5, 'center_y': 0.5}))
            self.add_widget(discard)
            for i, rolling_card in enumerate(myDeck.last_draw.modifiers):
                cx = 0.9 - (0.2 * (i / 5))
                cy = 0.9 - (0.2 * (i % 5))
                rolling =\
                    SpecificCard(
                        modifier_image=rolling_card.main_image,
                        element_image=rolling_card.element_image,
                        status_image=rolling_card.status_effect_image,
                        rolling_image=rolling_card.rolling_image,
                        class_image=rolling_card.character_class_image,
                        size_hint_x=(.2),
                        size_hint_y=(.2),
                        pos_hint=({'center_y': cy, 'center_x': cx}))
                self.add_widget(rolling)
        else:
            card_one = myDeck.last_draw.cards[0]
            if len(myDeck.last_draw.cards) == 2:
                card_two = myDeck.last_draw.cards[1]
                if card_one.is_this_card_better_than_me(card_two):
                    main_card = card_two
                    secondary_card = card_one
                    secondary_card_opacity = 0.3
                else:
                    main_card = card_one
                    secondary_card = card_two
                    secondary_card_opacity = 0.3
            elif myDeck.last_draw.draw_type == "advantage":
                main_card = card_one
                secondary_card = myDeck.last_draw.modifiers[0]
                secondary_card_opacity = 1
                rolling_opacity = 1
            else:  # disadvantage
                main_card = card_one
                secondary_card = myDeck.last_draw.modifiers[0]
                secondary_card_opacity = 0.3
                rolling_opacity = 0.3
                # print("secondary_card", secondary_card.value)
                # print("2nd better?",
                # card_one.is_this_card_better_than_me(secondary_card))
            discard_main_card = SpecificCard(
                modifier_image=main_card.main_image,
                element_image=main_card.element_image,
                status_image=main_card.status_effect_image,
                rolling_image=main_card.rolling_image,
                class_image=main_card.character_class_image,
                size_hint_x=(.65),
                size_hint_y=(.65),
                pos_hint=({'center_x': 0.3, 'center_y': 0.3})
            )
            discard_secondary_card = SpecificCard(
                modifier_image=secondary_card.main_image,
                element_image=secondary_card.element_image,
                status_image=secondary_card.status_effect_image,
                rolling_image=secondary_card.rolling_image,
                class_image=secondary_card.character_class_image,
                size_hint_x=(.45),
                size_hint_y=(.45),
                my_opacity=secondary_card_opacity,
                pos_hint=({'center_x': 0.7, 'center_y': 0.7})
            )
            self.add_widget(discard_secondary_card)
            self.add_widget(discard_main_card)
            if len(myDeck.last_draw.modifiers) > 1:
                for i, rolling_card in enumerate(
                        myDeck.last_draw.modifiers[1:]):
                    if i < 5:
                        cx = 0.1 + (0.2 * (i / 2))
                        cy = 0.9 - (0.2 * (i % 2))
                    else:
                        cx = 0.7 - (0.2 * ((4 - i) / 2))
                        cy = 0.38 - (0.2 * ((4 - i) % 2))
                    # cx = 0.7 + (0.2 * (i / 2))
                    # cy = 0.38 - (0.2 * (i % 2))
                    rolling =\
                        SpecificCard(
                            modifier_image=rolling_card.main_image,
                            element_image=rolling_card.element_image,
                            status_image=rolling_card.status_effect_image,
                            rolling_image=rolling_card.rolling_image,
                            class_image=rolling_card.character_class_image,
                            size_hint_x=(.2),
                            size_hint_y=(.2),
                            my_opacity=rolling_opacity,
                            pos_hint=({'center_y': cy, 'center_x': cx}))
                    self.add_widget(rolling)


class DeckApp(App):
    """Make the main window."""

    def build(self):
        """Give deck screen to app."""
        return MainDeckScreen()


myDeck = deck.Deck("deck_name", "brute")


if __name__ == '__main__':
    DeckApp().run()
