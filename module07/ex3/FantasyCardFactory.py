from typing import List, Dict, Union
import random
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard


class FantasyCardFactory(CardFactory):
    """Class to create random Card"""

    def __init__(self) -> None:
        """Initialize a FantasyCardFactory"""

        super().__init__()
        self.creatures: List[Dict[str, Union[str, int]]] = [
            {"name": "Fire Dragon", "cost": 5,
                "rarity": "Legendary", "attack": 7, "health": 5},
            {"name": "Goblin Warrior", "cost": 2,
                "rarity": "Common", "attack": 2, "health": 1},
            {"name": "Ice Wizard", "cost": 4,
                "rarity": "Rare", "attack": 3, "health": 4}
        ]
        self.spells: List[Dict[str, Union[str, int]]] = [
            {"name": "Lightning Bolt", "cost": 3,
                "rarity": "Common", "effect_type": "damage"},
            {"name": "Healing Potion", "cost": 2,
                "rarity": "Common", "effect_type": "heal"},
            {"name": "Fireball", "cost": 4,
                "rarity": "Uncommon", "effect_type": "damage"}
        ]
        self.artifacts: List[Dict[str, Union[str, int]]] = [
            {"name": "Mana Crystal", "cost": 2, "rarity": "Common",
                "durability": 5, "effect": "Permanent: +1 mana per turn"},
            {"name": "Sword of Power", "cost": 3, "rarity": "Uncommon",
                "durability": 3,
                "effect": "Permanent: +2 attack to equipped creature"},
            {"name": "Ring of Wisdom", "cost": 4, "rarity": "Rare",
                "durability": 4,
                "effect": "Permanent: Draw an extra card each turn"}
        ]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create a random creature card

        Args:
            name_or_power (str | int | None, optional):
                the name or attack of creature.
                Defaults to None.

        Raises:
            TypeError: if name or power is not a str or int
            TypeError: if can't access to attribute

        Returns:
            Card: The card created
        """

        try:
            if not name_or_power:
                creature = random.choice(self.creatures)

            else:
                if isinstance(name_or_power, str):
                    creatures = [
                        creature for creature
                        in self.creatures
                        if creature["name"] == name_or_power
                    ]
                    creature = random.choice(creatures)
                elif isinstance(name_or_power, int):
                    creatures = [
                        creature for creature
                        in self.creatures
                        if creature["attack"] == name_or_power
                    ]
                    creature = random.choice(creatures)
                else:
                    raise TypeError("Name or power is not an int or str")

            card = CreatureCard(creature["name"],
                                creature["cost"],
                                creature["rarity"],
                                creature["attack"],
                                creature["health"])
            return card
        except TypeError as e:
            raise TypeError(e)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create a random spell card

        Args:
            name_or_power (str | int | None, optional):
                the name or attack of spell.
                Defaults to None.

        Raises:
            TypeError: if name or power is not a str or int
            TypeError: if can't access to attribute

        Returns:
            Card: The card created
        """

        try:
            if not name_or_power:
                spell = random.choice(self.spells)

            else:
                if isinstance(name_or_power, str):
                    spells = [
                        spell for spell
                        in self.spells
                        if spell["name"] == name_or_power
                    ]
                    spell = random.choice(spells)

                else:
                    raise TypeError("Name or power is not an int or str")

            card = SpellCard(spell["name"],
                             spell["cost"],
                             spell["rarity"],
                             spell["effect_type"])
            return card
        except TypeError as e:
            raise TypeError(e)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create a random artifact card

        Args:
            name_or_power (str | int | None, optional):
                the name or attack of artifact.
                Defaults to None.

        Raises:
            TypeError: if name or power is not a str or int
            TypeError: if can't access to attribute

        Returns:
            Card: The card created
        """

        try:
            if not name_or_power:
                artifact = random.choice(self.artifacts)

            else:
                if isinstance(name_or_power, str):
                    artifacts = [
                        artifact for artifact
                        in self.artifacts
                        if artifact["name"] == name_or_power
                    ]
                    artifact = random.choice(artifacts)

                else:
                    raise TypeError("Name or power is not an int or str")

            card = ArtifactCard(artifact["name"],
                                artifact["cost"],
                                artifact["rarity"],
                                artifact["durability"],
                                artifact["effect"])
            return card
        except TypeError as e:
            raise TypeError(e)

    def create_themed_deck(self, size: int) -> dict:
        pass

    def get_supported_types(self) -> dict:
        pass

    def get_info(self) -> str:
        """Return the type of class

        Returns:
            str: Fantasy Factory
        """

        return "Fantasy Factory"
