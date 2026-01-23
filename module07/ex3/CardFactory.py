"""Abstract factory interfaces for creating card objects used by the card game.

Concrete factories should implement creation methods returning Card instances
or themed deck templates.
"""
from abc import ABC, abstractmethod
from ex0.Card import Card
from typing import Dict, List


class CardFactory(ABC):
    """Abstract factory interface for creating different types of cards."""

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create a creature card by name, attack power or randomly."""
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create a spell card by name or randomly."""
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create an artifact card by name or randomly."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict[str, List[dict]]:
        """Create a themed deck composed of template dictionaries."""
        pass

    @abstractmethod
    def get_supported_types(self) -> Dict[str, List[str]]:
        """Return the supported card type names."""
        pass

    def get_info(self) -> str:
        """Return the type description of this factory base class."""
        return "Card Factory"
