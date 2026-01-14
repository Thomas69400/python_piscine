from abc import ABC, abstractmethod


class Combatable(ABC):
    """Abstract class Combatable

    Args:
        ABC (ABC): Parent
    """

    @abstractmethod
    def attack(self, target) -> dict:
        """Deal damage to a target

        Args:
            target (Card): A card

        Raises:
            TypeError: if can't access to the attribute

        Returns:
            dict: a resume of what happened
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
