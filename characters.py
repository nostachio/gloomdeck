"""Character class.

Define perks for characters.
"""
from cards import Card
from cards import Character_Card
from perks import Perk


class Character_Class:
    """Character_Class definition."""

    def __init__(self, character_class):
        """Initialize attributes."""
        self.character_class = character_class
        self.character_class_image = self.select_character_class_image()
        self.perks = []
        self.determine_perks()

    def select_character_class_image(self):
        """Select class image."""
        character_class_image = "images/{0}.png".format(self.character_class)
        return character_class_image

    def determine_perks(self):
        """Determine what perks the character has access to."""
        # self.perks.append(
        #     Perk("sunkeeper",
        #          [
        #              Character_Card(1, "sunkeeper", True, None, None),
        #              Character_Card(1, "sunkeeper", True, None, None)
        #          ],
        #          []
        #          )
        # )
        # for perk in all_perks:
        #     if perk[0] == self.character_class:
        #         self.perks.append(Perk(perk[0], perk[1], perk[2]))
        class_perks = class_dictionary[self.character_class]
        print(class_perks)
        for perk in class_perks:
            print(perk)
            print(perk[0])
            print(perk[1])
            self.perks.append(Perk(perk[0], perk[1]))


# "character_class", [add_cards], [remove_cards]
# for list in all_perks:

# Perk("sunkeeper", [Character_Card(1, "sunkeeper", True, None, None),
#                Character_Card(1, "sunkeeper", True, None, None)], [])

sunkeeper_perks = [
    [
        [], [-1, -1]
    ],
    [
        [], [-1, -1]
    ],
    [
        [], [0, 0, 0, 0]
    ],
    [
        [Card(0)], [-2]
    ],
    [
        [Card(2)], [0]
    ],
    [
        [Character_Card(1, "sunkeeper", True, None, None),
         Character_Card(1, "sunkeeper", True, None, None)], []
    ],
    [
        [Character_Card(1, "sunkeeper", True, None, None),
         Character_Card(1, "sunkeeper", True, None, None)], []
    ],
    [
        [Character_Card(0, "sunkeeper", True, "heal1", None),
         Character_Card(0, "sunkeeper", True, "heal1", None)], []
    ],
    [
        [Character_Card(0, "sunkeeper", True, "heal1", None),
         Character_Card(0, "sunkeeper", True, "heal1", None)], []
    ],
    [
        [Character_Card(0, "sunkeeper", True, "stun", None)], []
    ],
    [
        [Character_Card(0, "sunkeeper", True, None, "light"),
         Character_Card(0, "sunkeeper", True, None, "light")], []
    ],
    [
        [Character_Card(0, "sunkeeper", True, None, "light"),
         Character_Card(0, "sunkeeper", True, None, "light")], []],
    [
        [Character_Card(0, "sunkeeper", True, "shield1", None),
         Character_Card(0, "sunkeeper", True, "shield1", None)], []
    ],
    [
        [Card(1), Card(1)], []
    ],
    [
        [], []
    ],
]
class_dictionary = {
    'sunkeeper': sunkeeper_perks
}
