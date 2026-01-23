from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict, Union


class EliteCard(Card, Combatable, Magical):
    """An elite card implementing both combat and magical interfaces.

    Combines the properties of a standard Card with Combatable and Magical
    interfaces, providing comprehensive combat and spell casting abilities.

    Args:
        Card (Card): Base card class.
        Combatable (Combatable): Combat interface.
        Magical (Magical): Magic interface.
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 combat_type: str, health: int,
                 damage: int, defense: int, mana: int) -> None:
        """Initialize an EliteCard that supports both combat and magic.

        Args:
            name (str): Card name.
            cost (int): Mana cost.
            rarity (str): Rarity descriptor.
            combat_type (str): Combat style/type.
            health (int): Health points.
            damage (int): Attack value.
            defense (int): Defense value.
            mana (int): Mana pool for spells.
        """

        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, damage, defense, health)
        self.combat_type: str = combat_type
        self.health: int = health
        self.damage: int = damage
        self.defense: int = defense
        self.mana: int = mana

    def play(self,
             game_state: Dict[str, Union[int, str]]) -> Dict[str, Union[str,
                                                                        int]]:
        """Play this elite card onto the battlefield and deduct mana."""

        try:
            play: Dict[str, Union[str, int]] = dict({
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "EliteCard played on terrain"
            })
            game_state["mana"] -= self.cost
            return play
        except TypeError as e:
            raise TypeError(e)

    def attack(self, target: Combatable) -> Dict[str, Union[str, int, bool]]:
        """Perform an attack against a Combatable target and return
        attack summary."""

        if not isinstance(target, Combatable):
            raise TypeError("Target is not Combatable")
        try:
            attack: Dict[str, Union[str, int, bool]] = dict({
                "attacker": self.name,
                "target": target.name,
                "damage": self.damage,
                "combat_type": self.combat_type
            })
            target.defend(self.damage)
            return attack
        except TypeError as e:
            raise TypeError(e)

    def defend(self, incoming_damage: int) -> Dict[str, Union[str, int, bool]]:
        """Defend against incoming damage and return defense summary."""

        try:
            damage = self.defense - incoming_damage
            if damage < 0:
                damage = 0
            attack: Dict[str, Union[str, int, bool]] = dict({
                "defender": self.name,
                "damage_taken": damage,
                "damage_blocked": self.defense,
                "still_alive": self.is_damage_to_kill(incoming_damage)
            })
            self.health -= self.defense - incoming_damage
            return attack
        except TypeError as e:
            raise TypeError(e)

    def get_combat_stats(self) -> Dict[str, Union[str, int]]:
        """Return combat statistics for this elite card."""

        stat = dict({
            "name": self.name,
            "combat_type": self.combat_type,
            "defense": self.defense,
            "attack": self.damage,
            "health": self.health
        })
        return stat

    def cast_spell(self,
                   spell_name: str,
                   targets: list[Combatable]) -> Dict[str,
                                                      Union[str,
                                                            int,
                                                            list]]:
        """Cast a spell affecting multiple targets and consume mana."""

        try:
            mana = 4
            spell = {
                "caster": self.name,
                "spell": spell_name,
                "targets": [target.name for target in targets],
                "mana_used": mana
            }
            self.mana -= mana
            return spell
        except TypeError as e:
            raise TypeError(e)

    def channel_mana(self, amount: int) -> Dict[str, Union[str, int]]:
        """Channel the given amount of mana into this card."""

        try:
            self.mana += amount
            channel = {
                "channeled": amount,
                "total_mana": self.mana
            }
            return channel
        except TypeError as e:
            raise TypeError(e)

    def get_magic_stats(self) -> Dict[str, Union[str, int]]:
        """Return magic-related statistics for this card."""

        stat = dict({
            "name": self.name,
            "mana": self.mana,
        })
        return stat

    def get_type(self) -> str:
        """Get the card type.

        Returns:
            str: The card type 'Elite Card'.
        """

        return "Elite Card"

    def is_damage_to_kill(self, damage: int) -> bool:
        """Determine whether the given damage would be lethal to this card."""

        try:
            return self.health <= damage
        except TypeError as e:
            raise TypeError(e)
