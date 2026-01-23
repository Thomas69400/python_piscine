from abc import ABC, abstractmethod
from typing import Dict, Union, List
from ex2.Combatable import Combatable


class Magical(ABC):
    """Abstract interface for cards that can cast spells and channel mana.

    Defines the contract for any card with magical abilities including
    spell casting, mana channeling, and magic statistics.
    """

    @abstractmethod
    def cast_spell(self, spell_name: str,
                   targets: List[Combatable]) -> Dict[str,
                                                      Union[str,
                                                            int,
                                                            List[str]]]:
        """Cast a spell on multiple targets.

        Args:
            spell_name (str): Name of the spell.
            targets (List[Combatable]): Targets to affect.

        Returns:
            Dict[str, Union[str, int, List[str]]]: Summary of the spell cast.
        """
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict[str, Union[str, int]]:
        """Channel mana into this card.

        Args:
            amount (int): Amount of mana to channel.

        Returns:
            Dict[str, Union[str, int]]: Summary including channeled amount
            and total mana.
        """
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict[str, Union[str, int]]:
        """Get this card's magic-related statistics.

        Returns:
            Dict[str, Union[str, int]]: Magic stats summary.
        """
        pass
