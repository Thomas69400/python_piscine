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

    def play(self,
             game_state: Dict[str, Union[int, str]]) -> Dict[str,
                                                             Union[str,
                                                                   int]]:
        """Summon this creature to the battlefield.

        Args:
            game_state (Dict[str, Union[int, str]]): The mutable game state
            (must contain 'mana').

        Returns:
            Dict[str, Union[str, int]]: Summary of the play action.
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

    def attack_target(self,
                      target: "CreatureCard") -> Dict[str,
                                                      Union[str,
                                                            int,
                                                            bool]]:
        """Attack a target creature and return the attack summary.

        Args:
            target (CreatureCard): The creature that is attacked.

        Returns:
            Dict[str, Union[str, int, bool]]: Summary including attacker,
            target, damage and whether the attack would kill.
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

    def is_damage_to_kill(self, target: "CreatureCard") -> bool:
        """Determine whether this creature's attack would kill the target.

        Args:
            target (CreatureCard): Creature being evaluated.

        Returns:
            bool: True if this attack is lethal, False otherwise.
        """

        try:
            if self.attack < target.health:
                return False
            return True
        except TypeError as e:
            raise TypeError(e)

    def get_card_info(self) -> Dict[str, Union[str, int]]:
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
