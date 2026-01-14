from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from typing import List, Dict, Union
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from ex0.Card import Card
from ex3.GameEngine import GameEngine


def main():
    """Execute program"""

    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")

    
    try:
        print("Factory: FantasyCardFactory")
        print("Strategy: AggressiveStrategy")
        factory = FantasyCardFactory()
        creatures: List[CreatureCard] = []
        spells: List[ArtifactCard] = []
        artifacts: List[SpellCard] = []
        for _ in range(2):
            creatures.append(factory.create_creature())
        spells.append(factory.create_spell())
        artifacts.append(factory.create_artifact())
        cards = {
            "creatures": [creature.name for creature
                          in creatures],
            "spells": [spell.name for spell
                       in spells],
            "artifacts": [artifact.name for artifact
                          in artifacts]
        }
        print(f"Available types: {cards}")
    except Exception as e:
        print(e)

    player1: Dict[
        str,
        Union[int, str, Deck, List[Card]]
    ] = {"health": 30, "mana": 20, "deck": Deck(),
         "hand": [], "battlefield": []}
    player1["deck"].add_card(creatures[0])
    player1["deck"].add_card(creatures[1])
    player1["deck"].add_card(spells[0])
    player1["deck"].add_card(artifacts[0])
    player1["hand"].append(player1["deck"].draw_card())
    player1["hand"].append(player1["deck"].draw_card())
    player1["hand"].append(player1["deck"].draw_card())
    player2: Dict[
        str,
        Union[int, str, Deck, List[Card]]
    ] = {"health": 30, "mana": 10, "deck": Deck(),
         "hand": [], "battlefield": []}
    try:
        print("\nSimulating aggressive turn..")
        print(f"Hand: {[card.get_value() for card in player1['hand']]}")
    except TypeError as e:
        print(f"Card in hand doesn't have attribute {e}")

    a_strat = AggressiveStrategy()
    print("\nTurn execution:")
    print(f"Strategy: {a_strat.get_strategy_name()}")


if __name__ == "__main__":
    main()
