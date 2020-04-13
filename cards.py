"""Card classes.

Class for cards and their methods.
"""


class Card:
    """Attack modifier card with only a numeric value or miss or double."""

    def __init__(self, value):
        """Initialize attributes."""
        self.value = str(value)
        self.main_image = self.select_main_image()
        self.is_rolling = False
        self.rolling_image = 'images/null.png'
        self.character_class = None
        self.character_class_image = 'images/null.png'
        self.status_effect = None
        self.status_effect_image = 'images/null.png'
        self.element = None
        self.element_image = 'images/null.png'
        self.main_image = self.select_main_image()

    def select_main_image(self):
        """Add corresponding image to card."""
        main_image = "images/{0}.png".format(self.value)
        return main_image

    def is_this_card_better_than_me(self, card_to_compare):
        """Return if the card is better, worse, or similar."""
        second_card_better = False
        if self.value == "miss" or self.value == "curse":
            second_card_better = True
        elif self.value == "2x" or self.value == "bless":
            second_card_better = False
        elif card_to_compare.value == "miss" or\
                card_to_compare.value == "curse":
            second_card_better = False
        elif card_to_compare.value == "2x" or card_to_compare.value == "bless":
            second_card_better = True
        elif card_to_compare.is_rolling:
            second_card_better = False
        else:
            if int(self.value) < int(card_to_compare.value):
                second_card_better = True
            elif int(self.value) == int(card_to_compare.value):
                if (
                    (
                        card_to_compare.status_effect is not None
                        or card_to_compare.element is not None
                    )
                    and
                    (
                        self.status_effect is not None
                        and self.element is not None
                    )
                ):
                    second_card_better = True
        return second_card_better

    def card_comparison(self, card_to_compare):
        """Return two cards after comparing them."""
        comparison_dictionary = {
            'better_card': None,
            'worse_card': None
        }
        second_card_better = False
        if self.value == "miss" or self.value == "curse":
            second_card_better = True
        elif self.value == "2x" or self.value == "bless":
            second_card_better = False
        elif card_to_compare.value == "miss" or\
                card_to_compare.value == "curse":
            second_card_better = False
        elif card_to_compare.value == "2x" or card_to_compare.value == "bless":
            second_card_better = True
        elif card_to_compare.is_rolling:
            second_card_better = False
        else:
            if int(self.value) < int(card_to_compare.value):
                second_card_better = True
            elif int(self.value) == int(card_to_compare.value):
                if (
                    (
                        card_to_compare.status_effect is not None
                        or card_to_compare.element is not None
                    )
                    and
                    (
                        self.status_effect is not None
                        and self.element is not None
                    )
                ):
                    second_card_better = True
        if second_card_better:
            comparison_dictionary['better_card'] = card_to_compare
            comparison_dictionary['worse_card'] = self
        else:
            comparison_dictionary['better_card'] = self
            comparison_dictionary['worse_card'] = card_to_compare
        return comparison_dictionary


class Character_Card(Card):
    """Cards added from perks."""

    def __init__(self, value, is_rolling, status_effect, element):
        """Initialize attributes."""
        self.value = str(value)
        self.is_rolling = is_rolling
        self.rolling_image = 'images/rolling.png'
        self.character_class = myDeck.character_class
        self.character_class_image = 'images/null.png'
        self.status_effect = status_effect
        self.element = element
        # self.main_image = 'images/0.png'
        self.main_image = self.select_main_image()
        # self.main_image = "images/{0}.png".format(self.value)
        self.status_effect_image = self.select_status_effect_image(
            status_effect)
        self.element_image = self.select_element_image(element)
        # print("character card")
        # print(self)

    # def select_main_image(self):
    #     """Add corresponding image to card."""
    #     main_image = "images/{0}.png".format(self.value)
    #     return main_image

    def select_status_effect_image(self, status_effect):
        """Pick image for status effect."""
        status_image = 'images/null.png'
        if self.status_effect is not None:
            status_image = "images/{0}.png".format(status_effect)
        return status_image

    def select_element_image(self, element):
        """Get the image for the element effect."""
        element_image = 'images/null.png'
        if self.element is not None:
            element_image = "images/{0}.png".format(element)
        return element_image


class Bless_Card(Card):
    """Bless Card."""

    def __init__(self):
        """Initialize attributes."""
        self.value = "bless"
        self.is_rolling = False
        self.rolling_image = 'images/null.png'
        self.status_effect_image = 'images/null.png'
        self.element_image = 'images/null.png'
        self.character_class_image = 'images/null.png'
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
        self.rolling_image = 'images/null.png'
        self.status_effect_image = 'images/null.png'
        self.element_image = 'images/null.png'
        self.character_class_image = 'images/null.png'


class Demerit_Card(Card):
    """Demerit Card."""

    def __init__(self):
        """Initialize attributes."""
        self.value = "-1"
        self.is_rolling = False
        self.character_class = None
        self.status_effect = None
        self.element = None
        self.main_image = self.select_main_image()
        self.rolling_image = 'images/null.png'
        self.status_effect_image = 'images/null.png'
        self.element_image = 'images/null.png'
        self.character_class_image = 'images/star.png'
