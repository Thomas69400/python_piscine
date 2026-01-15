from ex0.Card import Card
from typing import Dict, Union


class CreatureCard(Card):
    """A card representing a creature that can attack other creatures.

    Extends the base Card class with combat mechanics including attack power,
    health points, and targeting capabilities.

    Args:
        Card (ABC): Parent abstract base class.
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        """Initialize a CreatureCard

        Args:
            name (str): name of CreatureCard
            cost (int): cost of CreatureCard
            rarity (str): rarity of CreatureCard
            attack (int): attack of CreatureCard
            health (int): health of CreatureCard
        """

        super().__init__(name, cost, rarity)
        if attack < 0 or health < 0:
            raise ValueError("Attack and health must be positive integers")
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: dict) -> dict:
        """Summon a creature to the battlefield

        Args:
            game_state (dict): the actual state of the game

        Raises:
            TypeError: if can't access to value

        Returns:
            dict: a dictionary of the play state
        """

        try:
            play: Dict[str, Union[str, int]] = dict({
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            })
            game_state["mana"] -= self.cost
            return play
        except TypeError as e:
            raise TypeError(e)

    def attack_target(self, target) -> dict:
        """Reduce health of target by attack of self

        Args:
            target (CreatureCard): The creature attacked

        Raises:
            TypeError: if can't access to value

        Returns:
            dict: the state of the attack
        """

        try:
            attack: Dict[str, Union[str, int, bool]] = dict({
                "attacker": self.name,
                "target": target.name,
                "damage_dealt": self.attack,
                "combat_resolved": self.is_damage_to_kill(target)
            })
            return attack
        except TypeError as e:
            raise TypeError(e)

    def is_damage_to_kill(self, target) -> bool:
        """Check if the attack of self is enough to kill the target

        Args:
            target (CreatureCard): the creature attacked

        Raises:
            TypeError: if can't access to value

        Returns:
            bool: True if it kill, false if it does not kill
        """

        try:
            if self.attack < target.health:
                return False
            return True
        except TypeError as e:
            raise TypeError(e)

    def get_card_info(self) -> dict:
        """Get the information of the Creature

        Returns:
            dict: information about the Creature
        """

        info = dict({
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "attack": self.attack,
            "health": self.health
        })
        return info

    def get_type(self) -> str:
        """Get the type of CreatureCard

        Returns:
            str: creature
        """

        return "Creature"
