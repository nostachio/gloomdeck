"""Attack modifier deck tracker for Gloomhaven.

Lorem Ipsum.
"""
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
# from kivy.uix.image import Image
from kivy.uix.label import Label
import deck
from kivy.uix.checkbox import CheckBox
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import DictProperty
from kivy.properties import BooleanProperty
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
Window.size = (360, 780)

myDeck = deck.Deck("deck_name")


class MainDeckScreen(Screen):
    """Create the deck screen."""


class MainDeckLayout(RelativeLayout):
    """Layout for main deck screen."""


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
        Discard.update(self.parent.parent.children[2])
        DiscardHistory.update_discard(self.parent.parent.children[1])
        DrawResult.update(self.parent.parent.children[3])
        TopButtons.update(self.parent.parent.children[4])


class DisadvantageButton(DrawButton):
    """Disadvantage Button Widget."""


class AdvantageButton(DrawButton):
    """Advantage Button Widget."""


class BlessButton(Button):
    """Class for bless button."""

    def update(self):
        """Change the label number to number of blesses in deck."""
        self.text = str(myDeck.count_blesses())

    def add_bless(self):
        """Add a bless card to the deck."""
        myDeck.add_bless()
        self.update()

    def remove_bless(self):
        """Remove bless from deck."""
        myDeck.remove_bless()
        self.update()


class CurseButton(Button):
    """Class for curse button."""

    def update(self):
        """Change the label number to number of curses in deck."""
        self.text = str(myDeck.count_curses())

    def add_curse(self):
        """Add a curse card to the deck."""
        myDeck.add_curse()
        self.update()

    def remove_curse(self):
        """Remove curse from deck."""
        myDeck.remove_curse()
        self.update()


class DemeritButton(Button):
    """Class for demerit button."""

    def update(self):
        """Change the label number to number of curses in deck."""
        self.text = str(myDeck.count_demerits())

    def add_demerit(self):
        """Add a demerit card to the deck."""
        myDeck.add_demerit()
        self.update()


class Deck(RelativeLayout):
    """Deck widget."""


class ShuffleButton(Button):
    """Shuffle Button Widget."""

    shuffle_disabled = BooleanProperty(True)

    def update(self):
        """Determine if shuffle is available."""
        if myDeck.needs_shuffling():
            self.shuffle_disabled = False
        else:
            self.shuffle_disabled = True

    def shuffle(self):
        """Shuffle the deck."""
        myDeck.shuffle()
        DiscardHistory.update_discard(self.parent.parent.children[1])
        TopButtons.update(self.parent.parent.children[4])
        self.parent.parent.children[3].clear_widgets()
        self.parent.parent.children[2].clear_widgets()


class DiscardHistory(RelativeLayout):
    """Discard pile widget."""

    def update_discard(self):
        """Display the last x cards in discard."""
        self.clear_widgets()
        for i, this_card in enumerate(reversed(myDeck.discard)):
            cx = (0.1 + (0.1 * (i % 9)))
            cy = 0.95 - (.25 * (i / 9))
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
            self.add_widget(this_card_widget)


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

    def update(self):
        """Display results of draw."""
        self.clear_widgets()
        # ensure there's not 0 elements in a column to prevent divide by zero
        self.add_widget(Label())
        results = myDeck.last_draw.result_line_attack()\
            + myDeck.last_draw.result_line_status()\
            + myDeck.last_draw.result_line_elements()
        for w in results:
            self.add_widget(w)


class Discard(RelativeLayout):
    """Discard Pile Widget."""

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
                card_dict = card_one.card_comparison(card_two)
                if myDeck.last_draw.draw_type == "advantage":
                    main_card = card_dict['better_card']
                    secondary_card = card_dict['worse_card']
                    secondary_card_opacity = 0.3
                else:
                    main_card = card_dict['worse_card']
                    secondary_card = card_dict['better_card']
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


class CharacterSelectButton(Button):
    """Button to open CharacterDropdown."""

    character_image = StringProperty('images/character_select.png')

    def update(self):
        """Set button image to currently selected character."""
        self.character_image = myDeck.character_class.image


class CharacterButton(Button):
    """Individual character buttons for the CharacterDropdown."""

    def select_character(self, character):
        """Set character."""
        myDeck.set_character(character)
        CharacterSelectButton.update(
            self.parent.parent.parent.get_screen(
                'main').children[0].children[7])
        self.parent.parent.parent.get_screen(
            'main').children[0].children[6].is_disabled = False


class CharacterLayout(GridLayout):
    """Layout for character selection screen."""


class CharacterScreen(Screen):
    """Screen for selecting character class."""


class DeckContentScreen(Screen):
    """Screen for showing what remains in the deck."""


class PerkSelectCheckbox(CheckBox):
    """Button for selecting perks."""

    perk_index = NumericProperty(0)
    is_disabled = BooleanProperty(False)

    def update(self):
        """Disable items if they need to be disabled."""
        self.disabled = myDeck.available_perks[self.perk_index].is_disabled
        if self.disabled is True:
            # self.active = False
            myDeck.available_perks[self.perk_index].added = False
        self.active = myDeck.available_perks[self.perk_index].added

    def check(self, check_instance, is_active):
        """Do the following when checkbox is checked."""
        if myDeck.character_class.character_class == "nightshroud":
            for x in [3, 4]:
                if myDeck.available_perks[x].added is True:
                    myDeck.available_perks[x+2].is_disabled = False
                else:
                    myDeck.available_perks[x+2].is_disabled = True

            if myDeck.available_perks[check_instance.perk_index].is_disabled:
                self.is_disabled = True
            for widget in self.parent.children:
                widget.update()
        if is_active:
            myDeck.available_perks[check_instance.perk_index].added = True
            for widget in self.parent.children:
                widget.update()
        else:
            myDeck.available_perks[check_instance.perk_index].added = False
            for widget in self.parent.children:
                widget.update()


class PerkLayout(GridLayout):
    """Layout for perk selection."""


class PerkSelectScreenButton(Button):
    """Button on main screen to select perks."""

    is_disabled = BooleanProperty(True)


class ReturnToMainScreenButton(Button):
    """Button to return to main screen."""

    def apply_perks(self):
        """Apply perk effects before returning to the main screen."""
        myDeck.add_active_perks()


class PerkSelectionScreen(Screen):
    """Screen for selecting perks."""

    def populate(self):
        """Add perks to perk screen."""
        self.clear_widgets()
        layout = PerkLayout()
        for index, item in enumerate(myDeck.available_perks):
            label_color = [0, 0, 0, 1]
            is_checked = False
            if item.added:
                is_checked = True
            checkbox = PerkSelectCheckbox(perk_index=index,
                                          is_disabled=item.is_disabled,
                                          active=is_checked)
            checkbox.bind(active=checkbox.check)
            layout.add_widget(checkbox)
            if item.is_disabled:
                label_color = [0, 0, 0, .5]
            perk_text = PerkLabel(text=item.description,
                                  perk_index=index, my_text_color=label_color)
            layout.add_widget(perk_text)
        back_button = ReturnToMainScreenButton()
        self.add_widget(back_button)
        self.add_widget(layout)


class PerkLabel(Label):
    """Labels for perk selection screen."""

    my_text_color = ListProperty([0, 0, 0, 1])
    perk_index = NumericProperty(0)

    def update(self):
        """Change text color if disabled."""
        if myDeck.available_perks[self.perk_index].is_disabled:
            self.my_text_color = [0, 0, 0, .5]
        else:
            self.my_text_color = [0, 0, 0, 1]


class DeckApp(App):
    """Make the main window."""

    def build(self):
        """Give deck screen to app."""
        screenmanager = ScreenManager()
        screenmanager.add_widget(MainDeckScreen(name="main"))
        screenmanager.add_widget(CharacterScreen(name="character"))
        screenmanager.add_widget(DeckContentScreen(name="deck_content"))
        screenmanager.add_widget(PerkSelectionScreen(name="perk_selection"))
        screenmanager.current = 'main'
        return screenmanager


if __name__ == '__main__':
    DeckApp().run()
