from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


def main() -> None:
    """Main function demonstrating the Deck system with multiple card types.

    Creates a deck with creatures, spells, and artifacts, then demonstrates
    drawing and playing cards with polymorphic behavior.
    """
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    game_stat = {"mana": 10}
    deck: Deck = Deck()
    creature: CreatureCard = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    spell: SpellCard = SpellCard(
        "Lightning Bolt", 3, "Rare", "Deal 3 damage to target")
    artifact: ArtifactCard = ArtifactCard("Mana Crystal", 2, "Common",
                                          5, "Permanent: +1 mana per turn")
    try:
        deck.add_card(spell)
        deck.add_card(artifact)
        deck.add_card(creature)
    except TypeError as e:
        print(f"Error adding card to deck: {e}")

    deck.shuffle()
    try:
        print(f"Deck stats: {deck.get_deck_stats()}")
    except ZeroDivisionError as e:
        print(f"Error getting info: {e}")

    print("\nDrawing and playing cards:\n")

    try:
        for _ in range(3):
            card: Card = deck.draw_card()
            print(f"Drew: {card.name} ({card.get_type()})")
            print(f"Play result: {card.play(game_stat)}\n")
    except IndexError as e:
        print(f"Error drawing card: {e}")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
