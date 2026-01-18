"""Entry point for the Fantasy Card Game demo.

This module configures a factory and a strategy, builds a small deck,
simulates a turn and prints a short report.
"""
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from typing import List
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.GameEngine import GameEngine


def main() -> None:
    """Configure the game engine, build a small deck, simulate a turn
    and print results.

    This function demonstrates usage of the abstract factory and strategy
    implementations supplied in the ex3 package.
    """

    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")

    try:
        print("Factory: FantasyCardFactory")
        print("Strategy: AggressiveStrategy")
        factory = FantasyCardFactory()
        strategy = AggressiveStrategy()
        creatures: List[CreatureCard] = []
        spells: List[ArtifactCard] = []
        artifacts: List[SpellCard] = []
        for _ in range(2):
            creatures.append(factory.create_creature())
        spells.append(factory.create_spell())
        artifacts.append(factory.create_artifact())
        print(f"Available types: {factory.get_supported_types()}")
    except Exception as e:
        print(e)

    player: GameEngine = GameEngine()
    player.configure_engine(factory, strategy)
    player.deck.add_card(creatures[0])
    player.deck.add_card(creatures[1])
    player.deck.add_card(spells[0])
    player.deck.add_card(artifacts[0])
    player.hand.append(player.deck.draw_card())
    player.hand.append(player.deck.draw_card())
    player.hand.append(player.deck.draw_card())

    try:
        print("\nSimulating aggressive turn..")
        print(f"Hand: {[card.get_value() for card in player.hand]}")
    except TypeError as e:
        print(f"Card in hand doesn't have attribute {e}")

    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    actions = player.simulate_turn()
    print(f"Actions : {actions}")

    print("\nGame Report:")
    report = player.get_engine_status()
    print(report)

    print("\nAbstract Factory + Strategy Pattern: " +
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
