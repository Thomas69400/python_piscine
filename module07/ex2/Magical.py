from abc import ABC, abstractmethod


class Magical(ABC):
    """Abstract class Magical

    Args:
        ABC (ABC): Parent
    """

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on multiple target

        Args:
            spell_name (str): the name of the spell
            targets (list): the targets to cast the spell on

        Raises:
            TypeError: if can't access the attribute

        Returns:
            dict: a resume of what append
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
