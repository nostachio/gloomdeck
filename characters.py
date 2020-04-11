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
        # print(class_perks)
        for perk in class_perks:
            # print(perk)
            # print(perk[0])
            # print(perk[1])
            self.perks.append(Perk(perk[0], perk[1]))


# [add_cards], [remove_cards]
# for list in all_perks:

# Perk([Character_Card(1, "sunkeeper", True, None, None),
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
        [Character_Card(0, "sunkeeper", True, "heal_self1", None),
         Character_Card(0, "sunkeeper", True, "heal_self1", None)], []
    ],
    [
        [Character_Card(0, "sunkeeper", True, "heal_self1", None),
         Character_Card(0, "sunkeeper", True, "heal_self1", None)], []
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
        [Character_Card(0, "sunkeeper", True, "shield_self1", None),
         Character_Card(0, "sunkeeper", True, "shield_self1", None)], []
    ],
    [
        [Card(1), Card(1)], []
    ],
    [
        [], []
    ],
]
brute_perks = [
    [
        [], [-1, -1]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(1, False, None, None),
         Character_Card(1, False, None, None)],
        []
    ],
    [
        [Character_Card(1, False, None, None),
         Character_Card(1, False, None, None)],
        []
    ],
    [
        [Character_Card(3, False, None, None)], []
    ],
    [
        [
            Character_Card(0, True, "push1", None),
            Character_Card(0, True, "push1", None),
            Character_Card(0, True, "push1", None)
        ],
        []
    ],
    [
        [
            Character_Card(0, True, "push1", None),
            Character_Card(0, True, "push1", None),
            Character_Card(0, True, "push1", None)
        ],
        []
    ],
    [
        [Character_Card(0, True, "pierce3", None),
         Character_Card(0, True, "pierce3", None)
         ],
        []
    ],
    [
        [
            Character_Card(0, True, "stun", None)
        ], []
    ],
    [
        [Character_Card(0, True, "stun", None)
         ], []
    ],
    [
        [
            Character_Card(0, True, "disarm", None),
            Character_Card(0, True, "muddle", None)
        ], []
    ],
    [
        [Character_Card(0, True, "target", None)], []
    ],
    [
        [Character_Card(0, True, "target", None)], []
    ],
    [
        [Character_Card(1, True, "shield_self1", None)], []
    ],
    [
        [Character_Card(1, False, None, None)], []
    ],
]
tinkerer_perks = [
    [
        [], [-1, -1]
    ],
    [
        [], [-1, -1]
    ],
    [
        [Character_Card(0, False, None, None)], [-2]
    ],
    [
        [Character_Card(1, False, None, None),
         Character_Card(1, False, None, None)], []
    ],
    [
        [Character_Card(3, False, None, None)], []
    ],
    [
        [Character_Card(0, True, None, "fire"),
         Character_Card(0, True, None, "fire")], []
    ],
    [
        [Character_Card(0, True, "muddle", None),
         Character_Card(0, True, "muddle", None),
         Character_Card(0, True, "muddle", None)], []
    ],
    [
        [Character_Card(1, False, "wound", None)], []
    ],
    [
        [Character_Card(1, False, "wound", None)], []
    ],
    [
        [Character_Card(1, False, "immobilize", None)], []
    ],
    [
        [Character_Card(1, False, "immobilize", None)], []
    ],
    [
        [Character_Card(1, False, "heal_self2", None)], []
    ],
    [
        [Character_Card(1, False, "heal_self2", None)], []
    ],
    [
        [Character_Card(0, False, "target", None)], []
    ],
    [
        [], []
    ],
]
spellweaver_perks = [
    [
        [], [0, 0, 0, 0]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(1, False, None, None),
         Character_Card(1, False, None, None)], []
    ],
    [
        [Character_Card(1, False, None, None),
         Character_Card(1, False, None, None)], []
    ],
    [
        [Character_Card(0, False, "stun", None)], []
    ],
    [
        [Character_Card(1, False, "wound", None)], []
    ],
    [
        [Character_Card(1, False, "immobilize", None)], []
    ],
    [
        [Character_Card(1, False, "curse", None)], []
    ],
    [
        [Character_Card(2, False, None, "fire")], []
    ],
    [
        [Character_Card(2, False, None, "fire")], []
    ],
    [
        [Character_Card(2, False, None, "ice")], []
    ],
    [
        [Character_Card(2, False, None, "ice")], []
    ],
    [
        [Character_Card(0, True, None, "earth"),
         Character_Card(0, True, None, "wind")], []
    ],
    [
        [Character_Card(0, True, None, "light"),
         Character_Card(0, True, None, "dark")], []],
]
cragheart_perks = [
    [
        [], [0, 0, 0, 0]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(2, False, None, None),
         Character_Card(2, False, None, None),
         Character_Card(-2, False, None, None)], []
    ],
    [
        [Character_Card(1, False, "immobilize", None)], []
    ],
    [
        [Character_Card(1, False, "immobilize", None)], []
    ],
    [
        [Character_Card(2, False, "muddle", None)], []
    ],
    [
        [Character_Card(2, False, "muddle", None)], []
    ],
    [
        [Character_Card(0, True, "push2", None),
         Character_Card(0, True, "push2", None)], []
    ],
    [
        [Character_Card(0, True, None, "earth"),
         Character_Card(0, True, None, "earth")], []
    ],
    [
        [Character_Card(0, True, None, "earth"),
         Character_Card(0, True, None, "earth")], []
    ],
    [
        [Character_Card(0, True, None, "wind"),
         Character_Card(0, True, None, "wind")], []
    ],
    [
        [], []
    ],
    [
        [], []
    ],
]
scoundrel_perks = [
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
        [Character_Card(0, False, None, None)], [-2]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(2, False, None, None)], [0]
    ],
    [
        [Character_Card(2, False, None, None)], [0]
    ],
    [
        [Character_Card(1, True, None, None),
         Character_Card(1, True, None, None)], []
    ],
    [
        [Character_Card(1, True, None, None),
         Character_Card(1, True, None, None)], []
    ],
    [
        [Character_Card(0, True, "pierce3", None),
         Character_Card(0, True, "pierce3", None)], []
    ],
    [
        [Character_Card(0, True, "poison", None),
         Character_Card(0, True, "poison", None)], []
    ],
    [
        [Character_Card(0, True, "poison", None),
         Character_Card(0, True, "poison", None)], []
    ],
    [
        [Character_Card(0, True, "muddle", None),
         Character_Card(0, True, "muddle", None)], []
    ],
    [
        [Character_Card(0, True, "invisible", None)], []
    ],
    [
        [], []
    ],
]
mindtheif_perks = [
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
        [Character_Card(2, False, None, None),
         Character_Card(2, False, None, None)], [1, 1]
    ],
    [
        [Character_Card(0, False, None, None)], [-2]
    ],
    [
        [Character_Card(2, False, None, "ice")], []
    ],
    [
        [Character_Card(2, False, None, "ice")], []
    ],
    [
        [Character_Card(1, True, None, None),
         Character_Card(1, True, None, None)], []
    ],
    [
        [Character_Card(1, True, None, None),
         Character_Card(1, True, None, None)], []
    ],
    [
        [Character_Card(0, True, "pull1", None),
         Character_Card(0, True, "pull1", None),
         Character_Card(0, True, "pull1", None)], []
    ],
    [
        [Character_Card(0, True, "muddle", None),
         Character_Card(0, True, "muddle", None),
         Character_Card(0, True, "muddle", None)], []
    ],
    [
        [Character_Card(0, True, "immobilize", None),
         Character_Card(0, True, "immobilize", None)], []
    ],
    [
        [Character_Card(0, True, "stun", None)], []
    ],
    [
        [Character_Card(0, True, "disarm", None),
         Character_Card(0, True, "muddle", None)], []
    ],
    [
        [], []
    ],
]
quartermaster_perks = [
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
        [Character_Card(2, False, None, None)], [0]
    ],
    [
        [Character_Card(2, False, None, None)], [0]
    ],
    [
        [Character_Card(1, True, None, None),
         Character_Card(1, True, None, None)], []
    ],
    [
        [Character_Card(1, True, None, None),
         Character_Card(1, True, None, None)], []
    ],
    [
        [Character_Card(0, True, "muddle", None),
         Character_Card(0, True, "muddle", None),
         Character_Card(0, True, "muddle", None)], []
    ],
    [
        [Character_Card(0, True, "pierce3", None),
         Character_Card(0, True, "pierce3", None)], []
    ],
    [
        [Character_Card(0, True, "stun", None)], []
    ],
    [
        [Character_Card(0, True, "target", None)], []
    ],
    [
        [Character_Card(0, False, "item", None)], []
    ],
    [
        [Character_Card(0, False, "item", None)], []
    ],
    [
        [Character_Card(0, False, "item", None)], []
    ],
    [
        [Character_Card(1, False, None, None),
         Character_Card(1, False, None, None)], []
    ],
]
summoner_perks = [
    [
        [], [-1, -1]
    ],
    [
        [Character_Card(0, False, None, None)], [-2]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(2, False, None, None)], []
    ],
    [
        [Character_Card(2, False, None, None)], []
    ],
    [
        [Character_Card(0, True, "wound", None),
         Character_Card(0, True, "wound", None)], []
    ],
    [
        [Character_Card(0, True, "poison", None),
         Character_Card(0, True, "poison", None)], []
    ],
    [
        [Character_Card(0, True, "heal_self1", None),
         Character_Card(0, True, "heal_self1", None)], []
    ],
    [
        [Character_Card(0, True, "heal_self1", None),
         Character_Card(0, True, "heal_self1", None)], []
    ],
    [
        [Character_Card(0, True, "heal_self1", None),
         Character_Card(0, True, "heal_self1", None)], []
    ],
    [
        [Character_Card(0, True, None, "fire"),
         Character_Card(0, True, None, "wind")], []
    ],
    [
        [Character_Card(0, True, None, "dark"),
         Character_Card(0, True, None, "earth")], []
    ],
    [
        [Character_Card(1, False, None, None),
         Character_Card(1, False, None, None)], []
    ]
]
nightshroud_perks = [
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
        [Character_Card(-1, False, None, "dark")], []
    ],
    [
        [Character_Card(-1, False, None, "dark")], []
    ],
    [
        [Character_Card(1, False, None, "dark")],
        [Character_Card(-1, False, None, "dark")]
    ],
    [
        [Character_Card(1, False, None, "dark")],
        [Character_Card(-1, False, None, "dark")]
    ],
    [
        [Character_Card(1, False, "invisible", None)], []
    ],
    [
        [Character_Card(1, False, "invisible", None)], []
    ],
    [
        [Character_Card(0, True, "muddle", None),
         Character_Card(0, True, "muddle", None),
         Character_Card(0, True, "muddle", None)], []
    ],
    [
        [Character_Card(0, True, "muddle", None),
         Character_Card(0, True, "muddle", None),
         Character_Card(0, True, "muddle", None)], []
    ],
    [
        [Character_Card(0, True, "heal_self1", None),
         Character_Card(0, True, "heal_self1", None)], []
    ],
    [
        [Character_Card(0, True, "curse", None),
         Character_Card(0, True, "curse", None)], []
    ],
    [
        [Character_Card(0, True, "target", None)], []
    ],
    [
        [Character_Card(1, False, None, None),
         Character_Card(1, False, None, None)], []
    ]
]
plagueherald_perks = [
    [
        [Character_Card(0, False, None, None)], [-2]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(2, False, None, None)], [0]
    ],
    [
        [Character_Card(2, False, None, None)], [0]
    ],
    [
        [Character_Card(1, False, None, None),
         Character_Card(1, False, None, None)], []
    ],
    [
        [Character_Card(1, False, None, "wind")], []
    ],
    [
        [Character_Card(1, False, None, "wind")], []
    ],
    [
        [Character_Card(1, False, None, "wind")], []
    ],
    [
        [Character_Card(0, True, "poison", None),
         Character_Card(0, True, "poison", None),
         Character_Card(0, True, "poison", None)], []
    ],
    [
        [Character_Card(0, True, "curse", None),
         Character_Card(0, True, "curse", None)], []
    ],
    [
        [Character_Card(0, True, "immobilize", None),
         Character_Card(0, True, "immobilize", None)], []
    ],
    [
        [Character_Card(0, False, "stun", None)], []
    ],
    [
        [Character_Card(0, False, "stun", None)], []
    ],
    [
        [Character_Card(1, False, None, None)], []
    ],
]
berserker_perks = [
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
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(2, True, None, None)], [0]
    ],
    [
        [Character_Card(2, True, None, None)], [0]
    ],
    [
        [Character_Card(0, True, "wound", None),
         Character_Card(0, True, "wound", None)], []
    ],
    [
        [Character_Card(0, True, "wound", None),
         Character_Card(0, True, "wound", None)], []
    ],
    [
        [Character_Card(0, True, "stun", None)], []
    ],
    [
        [Character_Card(0, True, "stun", None)], []
    ],
    [
        [Character_Card(1, True, "disarm", None)], []
    ],
    [
        [Character_Card(0, True, "heal_self1", None),
         Character_Card(0, True, "heal_self1", None)], []
    ],
    [
        [Character_Card(2, False, None, "fire")], []
    ],
    [
        [Character_Card(2, False, None, "fire")], []
    ]
]
soothsinger_perks = [
    [
        [], [-1, -1]
    ],
    [
        [], [-1, -1]
    ],
    [
        [], [-2]
    ],
    [
        [Character_Card(4, False, None, None)], [1, 1]
    ],
    [
        [Character_Card(4, False, None, None)], [1, 1]
    ],
    [
        [Character_Card(1, False, "immobilize", None)], [0]
    ],
    [
        [Character_Card(1, False, "disarm", None)], [0]
    ],
    [
        [Character_Card(2, False, "wound", None)], [0]
    ],
    [
        [Character_Card(2, False, "poison", None)], [0]
    ],
    [
        [Character_Card(2, False, "curse", None)], [0]
    ],
    [
        [Character_Card(3, False, "muddle", None)], [0]
    ],
    [
        [Character_Card(0, False, "stun", None)], [-1]
    ],
    [
        [Character_Card(1, True, None, None),
         Character_Card(1, True, None, None),
         Character_Card(1, True, None, None)], []
    ],
    [
        [Character_Card(0, True, "curse", None),
         Character_Card(0, True, "curse", None)], []
    ],
    [
        [Character_Card(0, True, "curse", None),
         Character_Card(0, True, "curse", None)], []
    ]
]
doomstalker_perks = [
    [
        [], [-1, -1]
    ],
    [
        [], [-1, -1]
    ],
    [
        [Character_Card(1, False, None, None),
         Character_Card(1, False, None, None)], [0, 0]
    ],
    [
        [Character_Card(1, False, None, None),
         Character_Card(1, False, None, None)], [0, 0]
    ],
    [
        [Character_Card(1, False, None, None),
         Character_Card(1, False, None, None)], [0, 0]
    ],
    [
        [Character_Card(1, True, None, None),
         Character_Card(1, True, None, None)], []
    ],
    [
        [Character_Card(1, True, None, None),
         Character_Card(1, True, None, None)], []
    ],
    [
        [Character_Card(2, False, "muddle", None)], []
    ],
    [
        [Character_Card(1, False, "poison", None)], []
    ],
    [
        [Character_Card(1, False, "wound", None)], []
    ],
    [
        [Character_Card(1, False, "immobilize", None)], []
    ],
    [
        [Character_Card(0, False, "stun", None)], []
    ],
    [
        [Character_Card(0, True, "target", None)], []
    ],
    [
        [Character_Card(0, True, "target", None)], []
    ],
    [
        [], []
    ],
]
sawbones_perks = [
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
        [Character_Card(2, False, None, None)], [0]
    ],
    [
        [Character_Card(2, False, None, None)], [0]
    ],
    [
        [Character_Card(2, True, None, None)], []
    ],
    [
        [Character_Card(2, True, None, None)], []
    ],
    [
        [Character_Card(1, False, "immobilize", None)], []
    ],
    [
        [Character_Card(1, False, "immobilize", None)], []
    ],
    [
        [Character_Card(0, True, "wound", None),
         Character_Card(0, True, "wound", None)], []
    ],
    [
        [Character_Card(0, True, "wound", None),
         Character_Card(0, True, "wound", None)], []
    ],
    [
        [Character_Card(0, True, "stun", None)], []
    ],
    [
        [Character_Card(0, True, "heal_self3", None)], []
    ],
    [
        [Character_Card(0, True, "heal_self3", None)], []
    ],
    [
        [Character_Card(0, False, "item", None)], []
    ]
]
elementalist_perks = [
    [
        [], [-1, -1]
    ],
    [
        [], [-1, -1]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(2, False, None, None)], [0]
    ],
    [
        [Character_Card(2, False, None, None)], [0]
    ],
    [
        [Character_Card(0, False, None, "fire"),
         Character_Card(0, False, None, "fire"),
         Character_Card(0, False, None, "fire")], []
    ],
    [
        [Character_Card(0, False, None, "ice"),
         Character_Card(0, False, None, "ice"),
         Character_Card(0, False, None, "ice")], []
    ],
    [
        [Character_Card(0, False, None, "wind"),
         Character_Card(0, False, None, "wind"),
         Character_Card(0, False, None, "wind")], []
    ],
    [
        [Character_Card(0, False, None, "earth"),
         Character_Card(0, False, None, "earth"),
         Character_Card(0, False, None, "earth")], []
    ],
    [
        [Character_Card(0, False, None, "fire"),
         Character_Card(0, False, None, "earth")], [0, 0]
    ],
    [
        [Character_Card(0, False, None, "ice"),
         Character_Card(0, False, None, "wind")], [0, 0]
    ],
    [
        [Character_Card(1, False, "push1", None),
         Character_Card(1, False, "push1", None)], []
    ],
    [
        [Character_Card(1, False, "wound", None)], []
    ],
    [
        [Character_Card(0, False, "stun", None)], []
    ],
    [
        [Character_Card(0, False, "target", None)], []
    ],
]
beast_tyrant_perks = [
    [
        [], [-1, -1]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(1, False, None, None)], [-1]
    ],
    [
        [Character_Card(2, False, None, None)], [0]
    ],
    [
        [Character_Card(2, False, None, None)], [0]
    ],
    [
        [Character_Card(1, False, "wound", None)], []
    ],
    [
        [Character_Card(1, False, "wound", None)], []
    ],
    [
        [Character_Card(1, False, "immobilize", None)], []
    ],
    [
        [Character_Card(1, False, "immobilize", None)], []
    ],
    [
        [Character_Card(0, True, "heal_self1", None),
         Character_Card(0, True, "heal_self1", None)], []
    ],
    [
        [Character_Card(0, True, "heal_self1", None),
         Character_Card(0, True, "heal_self1", None)], []
    ],
    [
        [Character_Card(0, True, "heal_self1", None),
         Character_Card(0, True, "heal_self1", None)], []
    ],
    [
        [Character_Card(0, True, None, "earth")], []
    ],
    [
        [], []
    ],
]
diviner_perks = [
    [
        [], [-1, -1]
    ],
    [
        [], [-1, -1]
    ],
    [
        [], [-2]
    ],
    [
        [Character_Card(3, False, "shield_self1", None)], [1, 1]
    ],
    [
        [Character_Card(3, False, "shield_self1", None)], [1, 1]
    ],
    [
        [Character_Card(1, False, "shield_ally1", None)], [0]
    ],
    [
        [Character_Card(2, False, None, "dark")], [0]
    ],
    [
        [Character_Card(2, False, None, "light")], [0]
    ],
    [
        [Character_Card(3, False, "muddle", None)], [0]
    ],
    [
        [Character_Card(3, False, "curse", None)], [0]
    ],
    [
        [Character_Card(2, False, "regenerate", None)], [0]
    ],
    [
        [Character_Card(1, False, "heal_ally2", None)], [-1]
    ],
    [
        [Character_Card(0, True, "heal_self1", None),
         Character_Card(0, True, "heal_self1", None)], []
    ],
    [
        [Character_Card(0, True, "curse", None),
         Character_Card(0, True, "curse", None)], []],
    [
        [Character_Card(1, False, None, None),
         Character_Card(1, False, None, None)], []
    ]
]
class_dictionary = {
    'sunkeeper': sunkeeper_perks,
    'brute': brute_perks,
    'tinkerer': tinkerer_perks,
    'spellweaver': spellweaver_perks,
    'cragheart': cragheart_perks,
    'scoundrel': scoundrel_perks,
    'mindtheif': mindtheif_perks,
    'quartermaster': quartermaster_perks,
    'summoner': summoner_perks,
    'nightshroud': nightshroud_perks,
    'plagueherald': plagueherald_perks,
    'berserker': berserker_perks,
    'soothsinger': soothsinger_perks,
    'doomstalker': doomstalker_perks,
    'sawbones': sawbones_perks,
    'elementalist': elementalist_perks,
    'beast_tyrant': beast_tyrant_perks,
    'diviner': diviner_perks
}
