from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import List, Dict, Union
from random import shuffle


class Deck:
    """Manages a collection of Card objects for card games.

    Provides functionality to add, remove, shuffle, and draw cards from
    a deck, as well as retrieve statistics about the deck composition.
    """

    def __init__(self) -> None:
        """Initialize an empty Deck.

        Creates an empty list to store Card objects.
        """

        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a Card to the Deck.

        Args:
            card (Card): A Card object to add to the deck.

        Raises:
            TypeError: If the card is not an instance of Card.
        """

        if isinstance(card, Card):
            self.cards.append(card)
        else:
            raise TypeError(f"{card} is not a Card")

    def remove_card(self, card_name: str) -> bool:
        """Remove a card from the deck by its name.

        Args:
            card_name (str): The name of the card to remove.

        Returns:
            bool: True if the card was successfully removed, False otherwise.
        """

        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Randomize the order of cards in the deck.

        Uses the random.shuffle function to reorder cards randomly.
        """

        shuffle(self.cards)

    def draw_card(self) -> Card:
        """Draw the first card from the deck and remove it.

        Raises:
            IndexError: If the deck is empty.

        Returns:
            Card: The card drawn from the top of the deck.
        """

        if not self.cards:
            raise IndexError("Cannot draw from empty deck")
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict[str, Union[int, float]]:
        """Get detailed statistics about the deck composition.

        Returns:
            Dict[str, Union[int, float]]: total_cards, creatures, spells,
            artifacts, avg_cost
        """

        if not self.cards:
            return {"total_cards": 0, "creatures": 0, "spells": 0,
                    "artifacts": 0, "avg_cost": 0.0}

        stat = {
            "total_cards": len(self.cards),
            "creatures": len([
                c for c in self.cards if isinstance(c, CreatureCard)
            ]),
            "spells": len([
                c for c in self.cards if isinstance(c, SpellCard)
            ]),
            "artifacts": len([
                c for c in self.cards if isinstance(c, ArtifactCard)
            ]),
            "avg_cost": sum(card.cost for card in self.cards) / len(self.cards)
        }
        return stat
