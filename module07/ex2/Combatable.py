from abc import ABC, abstractmethod


class Combatable(ABC):
    """Abstract interface for cards that can engage in combat.

    Defines the contract for any card that can attack, defend,
    and provide combat statistics.

    Args:
        ABC (ABC): Abstract base class parent.
    """

    def __init__(self, damage: int, defense: int, health: int) -> None:
        self.health: int = health
        self.damage: int = damage
        self.defense: int = defense

    @abstractmethod
    def attack(self, target: 'Combatable') -> dict:
        """Deal damage to a target combatable card.

        Args:
            target (Combatable): A Combatable card to attack.

        Raises:
            TypeError: If unable to access card attributes.

        Returns:
            dict: Information about the attack result.
        """

        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Defend from damage taken

        Args:
            incoming_damage (int): the damage taken

        Raises:
            TypeError: if can't access attribute

        Returns:
            dict: a resume of what happened
        """

        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Get all the combat stats of the card

        Returns:
            dict: resume information of combat stats
        """

        pass
