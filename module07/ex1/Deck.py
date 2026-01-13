from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import List
from random import shuffle


class Deck:
    """Manage Cards"""

    def __init__(self):
        """Initialize a Deck"""

        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a Card to the Deck

        Args:
            card (Card): a Card

        Raises:
            TypeError: if card is not a Card
        """

        if isinstance(card, Card):
            self.cards.append(card)
        else:
            raise TypeError(f"{card} is not a Card")

    def remove_card(self, card_name: str) -> bool:
        """Remove a card from deck by the name

        Args:
            card_name (str): the name of the card

        Returns:
            bool: True if the card has been removed, false if not
        """

        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Randomize the deck"""

        shuffle(self.cards)

    def draw_card(self) -> Card:
        """Draw a card from deck

        Raises:
            IndexError: If no card in deck

        Returns:
            Card: the Card drew
        """

        try:
            drew = self.cards[0]
            self.remove_card(drew.name)
            return drew
        except IndexError as e:
            raise IndexError(e)

    def get_deck_stats(self) -> dict:
        """Resume information about Deck in a dict

        Raises:
            ZeroDivisionError: if no value in list

        Returns:
            dict: information on Deck
        """

        try:
            stat = {
                "total_cards": len(self.cards),
                "creatures": len([
                    c for c
                    in self.cards
                    if isinstance(c, CreatureCard)
                ]),
                "spells": len([
                    c for c
                    in self.cards
                    if isinstance(c, SpellCard)
                ]),
                "artifacts": len([
                    c for c
                    in self.cards
                    if isinstance(c, ArtifactCard)
                ]),
                "avg_cost": float(int(sum([
                    card.cost for card
                    in self.cards])/len(self.cards)+0.9))
            }
            return stat
        except ZeroDivisionError as e:
            raise ZeroDivisionError(e)
