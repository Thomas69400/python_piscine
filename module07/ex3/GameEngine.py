from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from typing import List, Optional, Dict, Union
from ex1.Deck import Deck


class GameEngine:
    """Engine that manages game state for simulation of turns.

    Attributes:
        turns (int): Class-level counter for simulated turns.
        card_played (int): Class-level counter for cards played.
        total_damage (int): Class-level total damage dealt.
        battlefield (List[Card]): Class-level battlefield list.
    """
    turns: int = 0
    card_played: int = 0
    total_damage: int = 0
    battlefield: List[Card] = []

    def __init__(self) -> None:
        """Initialize a new GameEngine instance with default resources."""
        self.strategy: Optional[GameStrategy] = None
        self.factory: Optional[CardFactory] = None
        self.deck: Deck = Deck()
        self.hand: List[Card] = []
        self.mana: int = 20
        self.health: int = 30

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Configure engine with a CardFactory and a GameStrategy.

        Args:
            factory (CardFactory): Factory used to create cards.
            strategy (GameStrategy): Strategy used to decide turn actions.
        """
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict[str, Union[int, str, list]]:
        """Simulate a single turn using the configured strategy.

        Returns:
            dict: Summary of the simulated turn provided by the strategy.
        """
        turn = self.strategy.execute_turn(self.hand, self.battlefield)
        self.card_played += len(turn["cards_played"])
        self.total_damage += turn["damage_dealt"]
        GameEngine.turns += 1
        return turn

    def get_engine_status(self) -> Dict[str, Union[int, str]]:
        """Return a summary of the engine's current aggregated status.

        Returns:
            dict: Contains keys 'turns_simulated', 'strategy_used',
            'total_damage', 'cards_created'.
        """
        status = {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.card_played
        }
        return status
