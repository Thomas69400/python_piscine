"""Abstract Card base class used by the simple card game examples.

Defines interface methods for play, inspection and simple helpers.
"""
from abc import ABC, abstractmethod
from typing import Dict, Union


class Card(ABC):
    """Abstract base class for all card types in the card game.

    Defines the interface that all cards must implement, including
    playing mechanics, mana cost checking, and card information retrieval.

    Args:
        ABC: Abstract base class parent.
    """

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Initialize a Card

        Args:
            name (str): name of Card
            cost (int): cost of Card
            rarity (str): rarity of Card
        """

        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self,
             game_state: Dict[str, Union[int, str]]) -> Dict[str,
                                                             Union[str,
                                                                   int]]:
        """Play a Card on the battlefield.

        Args:
            game_state (Dict[str, Union[int, str]]): Mutable game state
            (must contain 'mana').

        Returns:
            Dict[str, Union[str, int]]: Summary of the play action (card name,
            mana used, effect).
        """

        try:
            play: Dict[str, Union[str, int]] = dict({
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Card played on terrain"
            })
            game_state["mana"] -= self.cost
            return play
        except TypeError as e:
            raise TypeError(e)

    def get_card_info(self) -> Dict[str, Union[str, int]]:
        """Get the information of the Card

        Returns:
            dict: information about the Card
        """
        info = dict({
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        })
        return info

    def is_playable(self, available_mana: int) -> bool:
        """Check if the mana available is enough to play the card

        Args:
            available_mana (int): the mana of player

        Raises:
            TypeError: if mana is not an int

        Returns:
            bool: True if can play, false if it can not
        """

        try:
            if self.cost <= available_mana:
                return True
            return False
        except TypeError as e:
            raise TypeError(e)

    def get_type(self) -> str:
        """Get the type of Card

        Returns:
            str: card
        """

        return "Card"

    def get_value(self) -> str:
        """Return the cost name and cost of card

        Returns:
            str: The name and cost of card
        """

        return f"{self.name} ({self.cost})"
