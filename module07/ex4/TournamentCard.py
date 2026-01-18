from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Dict, Union, List


class TournamentCard(Card, Combatable, Rankable):
    """A card used in tournament matches combining Card,
    Combatable and Rankable."""

    def __init__(self, name: str, cost: int, rarity: str, damage: int,
                 defense: int, health: int, card_id: str, rating: int) -> None:
        """Initialize a TournamentCard.

        Args:
            name (str): Card name.
            cost (int): Mana or cost to play.
            rarity (str): Rarity descriptor.
            damage (int): Damage value for combat.
            defense (int): Defense value for combat.
            health (int): Health points.
            card_id (str): Unique identifier.
            rating (int): Initial rating for ranking.
        """
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, damage, defense, health)
        Rankable.__init__(self, rating)
        self.id: str = card_id

    def play(self, game_state: Dict[
            str, Union[int, str]]) -> Dict[str, Union[str, int]]:
        """Play this card, applying its cost to the provided game state.

        Args:
            game_state (dict): Mutable game state containing at least 'mana'.

        Returns:
            dict: A short description of the play action.
        """
        try:
            play: Dict[str, Union[str, int]] = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "EliteCard played on terrain"
            }
            game_state["mana"] -= self.cost
            return play
        except TypeError as e:
            raise TypeError(e)

    def attack(self, target: Combatable) -> Dict[str, Union[str, int, bool]]:
        """Attack a Combatable target.

        Args:
            target (Combatable): The target to attack.

        Returns:
            dict: Attack summary including attacker, target,
            damage and defense result.
        """
        if not isinstance(target, Combatable):
            raise TypeError("Target is not Combatable")
        try:
            attack: Dict[str, Union[str, int, bool]] = {
                "attacker": self.name,
                "target": target.name,
                "damage": self.damage,
            }
            attack.update({"defense": target.defend(self.damage)})
            return attack
        except TypeError as e:
            raise TypeError(e)

    def defend(self, incoming_damage: int) -> Dict[str, Union[str, int, bool]]:
        """Defend against incoming damage and update health accordingly.

        Args:
            incoming_damage (int): Damage incoming from an attacker.

        Returns:
            dict: Defense result including damage taken,
            blocked amount and alive flag.
        """
        try:
            damage = incoming_damage - self.defense
            if damage < 0:
                damage = 0
            attack: Dict[str, Union[str, int, bool]] = {
                "defender": self.name,
                "damage_taken": damage,
                "damage_blocked": self.defense,
                "still_alive": self.is_damage_to_kill(damage)
            }
            self.health -= damage
            return attack
        except TypeError as e:
            raise TypeError(e)

    def get_combat_stats(self) -> Dict[str, Union[str, int]]:
        """Return combat-related statistics for this card."""
        stat: Dict[str, Union[str, int]] = {
            "name": self.name,
            "combat_type": self.combat_type,
            "defense": self.defense,
            "attack": self.damage,
            "health": self.health
        }
        return stat

    def calculate_rating(self) -> int:
        """Update and return the rating based on wins and losses.

        Returns:
            int: Updated rating.
        """
        rating_delta: int = self.wins * 5 - self.losses * 2
        self.rating += rating_delta
        return self.rating

    def get_tournament_stats(self) -> Dict[str, Union[str, int, List[str]]]:
        """Return a dictionary of tournament-related stats
        for external reporting."""
        stats: Dict[str, Union[str, int, List[str]]] = {
            "id": self.id,
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.rating,
            "interfaces": ["Card", "Combatable", "Rankable"]
        }
        return stats

    def update_wins(self, wins: int) -> None:
        """Increment wins counter.

        Args:
            wins (int): Number of wins to add.
        """
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        """Increment losses counter.

        Args:
            losses (int): Number of losses to add.
        """
        self.losses += losses

    def get_rank_info(self) -> Dict[str, int]:
        """Return ranking information for this card."""
        info: Dict[str, int] = {
            "rank": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }
        return info

    def is_damage_to_kill(self, damage: int) -> bool:
        """Check whether the given damage would result in death.

        NOTE: existing implementation compares current health against damage.

        Args:
            damage (int): The damage to evaluate.

        Returns:
            bool: True if card remains alive (per existing logic),
            False otherwise.
        """
        try:
            return self.health > damage
        except TypeError as e:
            raise TypeError(e)
