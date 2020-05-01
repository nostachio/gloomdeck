"""Card classes.

Class for cards and their methods.
"""


class Card:
    """Attack modifier card with only a numeric value or miss or double."""

    def __init__(self, value=0, type="standard", is_rolling=False,
                 status_effect=None, element=None, character_class=None):
        """Initialize attributes."""
        # type: None (standard deck card), perk (from character's perk deck),
        # bless, curse, demerit (additional -1 from scenarios or items)
        self.type = type
        self.value = str(value)
        self.is_rolling = is_rolling
        self.character_class = character_class
        self.status_effect = status_effect
        self.element = element
        self.derive_images()

    def derive_images(self):
        """Set all image paths."""
        self.main_image = self.select_main_image()
        self.rolling_image = self.select_rolling_image()
        self.character_class_image = self.select_character_class_image()
        self.status_effect_image = self.select_status_effect_image()
        self.element_image = self.select_element_image()

    def select_main_image(self):
        """Add corresponding value image to card."""
        # make this display element or status effect on 0 cards
        main_image = "images/{0}.png".format(self.value)
        return main_image

    def select_character_class_image(self):
        """Add corresponding character class image to card."""
        if self.character_class is not None:
            image = "images/{0}.png".format(self.character_class)
        elif self.type == "demerit":
            image = "images/star.png"
        else:
            image = "images/null.png"
        return image

    def select_status_effect_image(self):
        """Add corresponding status effect image to card."""
        if self.status_effect is not None:
            image = "images/{0}.png".format(self.status_effect)
        else:
            image = "images/null.png"
        return image

    def select_element_image(self):
        """Add corresponding image to card."""
        if self.element is not None:
            image = "images/{0}.png".format(self.element)
        else:
            image = "images/null.png"
        return image

    def select_rolling_image(self):
        """Add corresponding rolling image to card."""
        if self.is_rolling:
            image = "images/rolling.png"
        else:
            image = "images/null.png"
        return image

    def is_this_card_better_than_me(self, card_to_compare):
        """Return if the card is better, worse, or similar."""
        # Use first card if 2nd is not better as per rules
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
