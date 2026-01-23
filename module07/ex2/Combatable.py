from abc import ABC, abstractmethod
from typing import Dict, Union


class Combatable(ABC):
    """Abstract interface for cards that can engage in combat.

    Defines the contract for any card that can attack, defend,
    and provide combat statistics.
    """

    def __init__(self, damage: int, defense: int, health: int) -> None:
        self.health: int = health
        self.damage: int = damage
        self.defense: int = defense

    @abstractmethod
    def attack(self, target: "Combatable") -> Dict[str, Union[str, int, bool]]:
        """Deal damage to a target combatable card.

        Args:
            target (Combatable): A combat-capable card to attack.

        Returns:
            Dict[str, Union[str, int, bool]]: Attack summary.
        """
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict[str, Union[str, int, bool]]:
        """Defend against incoming damage.

        Args:
            incoming_damage (int): Amount of incoming damage.

        Returns:
            Dict[str, Union[str, int, bool]]: Defense summary including damage
            taken and alive flag.
        """
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict[str, Union[str, int]]:
        """Return combat-related statistics for the card.

        Returns:
            Dict[str, Union[str, int]]: Combat stats such as name, attack,
            defense, health.
        """
        pass
