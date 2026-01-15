from abc import ABC, abstractmethod
from ex2.Combatable import Combatable


class Magical(ABC):
    """Abstract interface for cards that can cast spells and channel mana.

    Defines the contract for any card with magical abilities including
    spell casting, mana channeling, and magic statistics.

    Args:
        ABC (ABC): Abstract base class parent.
    """

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list[Combatable]) -> dict:
        """Cast a spell on multiple targets.

        Args:
            spell_name (str): The name of the spell to cast.
            targets (list[Combatable]): The target cards to cast the spell on.

        Raises:
            TypeError: If unable to access card attributes.

        Returns:
            dict: Information about the spell cast.
        """

        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Channel mana

        Args:
            amount (int): the amount of mana channeled

        Raises:
            TypeError: if the amount is not an int

        Returns:
            dict: a resume of what happened
        """

        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Get the stat of magic of card

        Returns:
            dict: a resume of magic stat
        """

        pass
