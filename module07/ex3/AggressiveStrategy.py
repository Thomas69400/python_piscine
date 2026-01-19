"""Aggressive play strategy for the card game.

This module implements a GameStrategy that prefers low-cost cards and
attacks aggressively. It exposes an execute_turn method that the GameEngine
uses to simulate a turn.
"""
from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from typing import List, Dict, Union, Sequence, Any


class AggressiveStrategy(GameStrategy):
    """A strategy that plays low-cost cards first and attacks aggressively."""

    def execute_turn(self,
                     hand: Sequence[Card],
                     battlefield: Sequence[Card]) -> Dict[
                         str, Union[int, str, list]]:
        """Execute an aggressive turn.

        - Prefer cards with cost <= 3.
        - If none, play all available cards.
        - Call play on each chosen card and sum damage from creature cards.
        - Choose targets via prioritize_targets.

        Args:
            hand: Sequence of Card objects representing the player's hand.
            battlefield: Sequence of Card objects representing opposing units.

        Returns:
            A dictionary summarizing the turn:
              {
                "cards_played": List[str],
                "mana_used": int,
                "targets_attacked": list,
                "damage_dealt": int
              }
        """
        cards: List[Card] = [
            card for card
            in hand
            if card.cost <= 3]

        if len(cards) == 0:
            cards = [
                card for card
                in hand]

        for card in cards:
            card.play({"mana": 20})

        targets: List[
            Union[CreatureCard,
                  str]] = self.prioritize_targets(list(battlefield))
        damage: int = sum(
            [card.attack for card in cards if isinstance(card, CreatureCard)])
        turn: Dict[str, Union[int, str, list]] = {
            "cards_played": [card.name for card in cards],
            "mana_used": sum([card.cost for card in cards]),
            "targets_attacked": targets,
            "damage_dealt": damage
        }
        return turn

    def get_strategy_name(self) -> str:
        """Return the name of this strategy."""
        return "Aggressive Strategy"

    def prioritize_targets(self,
                           available_targets: Sequence[Any]) -> List[
                               Union[CreatureCard, str]]:
        """Prioritize available targets for attack.

        If no targets exist, returns ['Enemy Player'].
        Otherwise prefers targets with health <= 3.

        Args:
            available_targets: Sequence of potential CreatureCard targets.

        Returns:
            A list of prioritized targets (CreatureCard instances) or the
            original available_targets if none match the preference. If
            available_targets is empty returns ['Enemy Player'].
        """
        if len(available_targets) == 0:
            return ["Enemy Player"]

        else:
            try:
                targets = [
                    target for target
                    in available_targets
                    if getattr(target, "health", None) is not None
                    and target.health <= 3
                ]

                if len(targets) == 0:
                    return list(available_targets)
                return targets

            except TypeError as e:
                return [e]
