from ex4.TournamentCard import TournamentCard
from typing import List, Dict, Union


class TournamentPlatform:
    """Platform to register tournament cards and run matches.

    Responsible for registering TournamentCard instances, running matches
    between registered cards, producing a leaderboard and generating a
    high-level platform report.
    """

    def __init__(self) -> None:
        """Initialize a new TournamentPlatform with empty registry."""
        self.cards: List[TournamentCard] = []
        self.match_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register a TournamentCard to the platform.

        Args:
            card (TournamentCard): Card to register.

        Returns:
            str: Confirmation message including card name and id.
        """
        self.cards.append(card)
        return f"Card {card.name} with ID {card.id} registered."

    def create_match(self, card1_id: str,
                     card2_id: str) -> Dict[str, Union[str, int]]:
        """Simulate a match between two registered cards identified by id.

        Args:
            card1_id (str): Identifier of the first card.
            card2_id (str): Identifier of the second card.

        Returns:
            dict: Summary of the match with winner/loser and ratings, or
                  an error dict if a card is not found.
        """
        self.match_played += 1
        try:
            creature1: TournamentCard = [
                card for card in self.cards if card.id == card1_id][0]
            creature2: TournamentCard = [
                card for card in self.cards if card.id == card2_id][0]
            attack = creature1.attack(creature2)
            attack2 = creature2.attack(creature1)
            match_summary: Dict[str, Union[str, int]] = {}
            if attack["defense"]["still_alive"] is False \
                    and attack2["defense"]["still_alive"] is True:
                creature1.update_wins(1)
                creature2.update_losses(1)
                match_summary.update({
                    "winner": creature1.name,
                    "loser": creature2.name,
                    "winner_rating": creature1.calculate_rating(),
                    "loser_rating": creature2.calculate_rating()})
            else:
                creature2.update_wins(1)
                creature1.update_losses(1)
                match_summary.update({
                    "winner": creature2.name,
                    "loser": creature1.name,
                    "winner_rating": creature2.calculate_rating(),
                    "loser_rating": creature1.calculate_rating()})
            return match_summary
        except IndexError:
            return {"error": "One or both cards not found"}

    def get_leaderboard(self) -> List[Dict[str, Union[str, int]]]:
        """Return a leaderboard of registered cards sorted by rating.

        Returns:
            list: List of leaderboard entries containing rank, name, id,
            rating, wins, losses.
        """
        cards = sorted(self.cards, key=lambda c: c.rating, reverse=True)
        leaderboard: List[Dict[str, Union[str, int]]] = []
        for rank, card in enumerate(cards, start=1):
            leaderboard.append({
                "rank": rank,
                "name": card.name,
                "id": card.id,
                "rating": card.rating,
                "wins": card.wins,
                "losses": card.losses
            })
        return leaderboard

    def generate_tournament_report(self) -> Dict[str, Union[int, float, str]]:
        """Generate a brief report about the tournament platform.

        Returns:
            dict: Report including total registered cards, matches played,
                  average rating and platform status.
        """
        total_cards = len(self.cards)
        average_rating: float = (
            sum(card.rating
                for card
                in self.cards) / total_cards) if total_cards > 0 else 0.0
        report: Dict[str, Union[int, float, str]] = {
            "total_cards": total_cards,
            "match_played": self.match_played,
            "average_rating": average_rating,
            "platform_status": "Active"
        }
        return report
