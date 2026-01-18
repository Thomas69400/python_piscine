from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):
    """Abstract base class defining rank-related behavior for objects."""

    def __init__(self, rating: int) -> None:
        """Initialize rankable counters and starting rating."""
        self.rating: int = rating
        self.wins: int = 0
        self.losses: int = 0

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return an updated rating."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update wins counter by the specified amount."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update losses counter by the specified amount."""
        pass

    @abstractmethod
    def get_rank_info(self) -> Dict[str, int]:
        """Return rank information as a dictionary containing keys like 'rank',
        'wins','losses'."""
        pass
