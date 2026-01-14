from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from typing import List


class GameEngine:
    turns: int = 0

    def __init__(self) -> None:
        self.strategy: GameStrategy = None
        self.factory: CardFactory = None
        self.hand: List[Card] = []
        self.battlefield: List[Card] = []
        self.enemy_battlefield: List[Card] = []

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        self.strategy.execute_turn(self.hand, self.enemy_battlefield)
        GameEngine.turns += 1

    def get_engine_status(self) -> dict:
        status = {
            "strategy": self.strategy.get_strategy_name(),
            "factory": self.factory.get_info()
        }
        return status
