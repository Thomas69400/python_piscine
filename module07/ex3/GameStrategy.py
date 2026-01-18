from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """Abstract base class that defines the interface for a game strategy.

    Concrete strategies must implement how a turn is executed, provide a name,
    and implement a simple target prioritization method.
    """

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute a turn using the provided hand and battlefield.

        Args:
            hand (list): List of Card objects representing the player's hand.
            battlefield (list): List of Card objects currently
            on the battlefield.

        Returns:
            dict: A dictionary summarizing the actions taken during the turn,
            e.g.
                  {"cards_played": [...], "mana_used": int, "targets_attacked":
                  [...], "damage_dealt": int}
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the human readable name of the strategy.

        Returns:
            str: Strategy name.
        """

        return "Game Strategy"

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Choose and order targets from the available targets.

        Args:
            available_targets (list): A list of potential targets
            (e.g. CreatureCard instances).

        Returns:
            list: A list of prioritized targets (may include the string
            'Enemy Player').
        """
        pass
