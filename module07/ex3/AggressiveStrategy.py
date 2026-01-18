from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from typing import List, Dict, Union


class AggressiveStrategy(GameStrategy):
    """A strategy that plays low-cost cards first and attacks aggressively."""

    def execute_turn(self, hand: list,
                     battlefield: list) -> Dict[str, Union[int, str, list]]:
        """Execute an aggressive turn.

        - Prefer cards with cost <= 3.
        - If none, play all available cards.
        - Play cards (call play) and sum damage from creatures.
        - Choose targets via prioritize_targets.

        Args:
            hand (list): Player's hand containing Card instances.
            battlefield (list): Opponent battlefield or similar targets.

        Returns:
            dict: Summary of the turn with keys 'cards_played', 'mana_used',
            'targets_attacked', 'damage_dealt'.
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

        targets: List[CreatureCard] = self.prioritize_targets(battlefield)
        damage: int = sum(
            [card.attack for card in cards if isinstance(card, CreatureCard)])
        turn: Dict[str, Union[str]] = {
            "cards_played": [card.name for card in cards],
            "mana_used": sum([card.cost for card in cards]),
            "targets_attacked": targets,
            "damage_dealt": damage
        }
        return turn

    def get_strategy_name(self) -> str:
        """Return the name of this strategy."""
        return "Aggressive Strategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """Prioritize available targets for attack.

        If no targets exist, returns ['Enemy Player'].
        Otherwise prefers targets with health <= 3.

        Args:
            available_targets (list): List of potential CreatureCard targets.

        Returns:
            list: Prioritized list of targets or the original list if none
            match the preference.
        """
        if len(available_targets) == 0:
            return ["Enemy Player"]

        else:
            try:
                targets = [
                    target for target
                    in available_targets
                    if target.health <= 3
                ]

                if len(targets) == 0:
                    return available_targets
                return targets

            except TypeError as e:
                return e
