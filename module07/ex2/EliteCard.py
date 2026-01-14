from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict, Union


class EliteCard(Card, Combatable, Magical):
    """EliteCard class

    Args:
        Card (Card): Parent
        Combatable (Combatable): Parent
        Magical (Magical): Parent
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 combat_type: str, health: int,
                 damage: int, defense: int, mana: int) -> None:
        """Initialize an EliteCard

        Args:
            name (str): the name of card
            cost (int): cost of card
            rarity (str): rarity of card
            combat_type (str): the combat type of card
            health (int): the health of card
            damage (int): the attack of card
            defense (int): the defense of card
            mana (int): the mana of card
        """

        super().__init__(name, cost, rarity)
        self.combat_type: str = combat_type
        self.health: int = health
        self.damage: int = damage
        self.defense: int = defense
        self.mana: int = mana

    def play(self, game_state: dict) -> dict:
        """Play a card on terrain

        Args:
            game_state (dict): the state of the game

        Raises:
            TypeError: if can't access to attribute

        Returns:
            dict: a resume of what append
        """

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

    def attack(self, target) -> dict:
        """Deal damage to a target

        Args:
            target (Card): A card

        Raises:
            TypeError: if can't access to the attribute

        Returns:
            dict: a resume of what happened
        """

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

    def defend(self, incoming_damage: int) -> dict:
        """Defend from damage taken

        Args:
            incoming_damage (int): the damage taken

        Raises:
            TypeError: if can't access attribute

        Returns:
            dict: a resume of what happened
        """

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

    def get_combat_stats(self) -> dict:
        """Get all the combat stats of the card

        Returns:
            dict: resume information of combat stats
        """

        stat = dict({
            "name": self.name,
            "combat_type": self.combat_type,
            "defense": self.defense,
            "attack": self.damage,
            "health": self.health
        })
        return stat

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell on multiple target

        Args:
            spell_name (str): the name of the spell
            targets (list): the targets to cast the spell on

        Raises:
            TypeError: if can't access the attribute

        Returns:
            dict: a resume of what append
        """

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

    def channel_mana(self, amount: int) -> dict:
        """Channel mana

        Args:
            amount (int): the amount of mana channeled

        Raises:
            TypeError: if the amount is not an int

        Returns:
            dict: a resume of what happened
        """

        try:
            self.mana += amount
            channel = {
                "channeled": 3,
                "total_mana": self.mana
            }
            return channel
        except TypeError as e:
            raise TypeError(e)

    def get_magic_stats(self) -> dict:
        """Get the stat of magic of card

        Returns:
            dict: a resume of magic stat
        """

        stat = dict({
            "name": self.name,
            "mana": self.mana,
        })
        return stat

    def get_type(self):
        """Get the type of the card

        Returns:
            _type_: Elite Card
        """

        return "Elite Card"

    def is_damage_to_kill(self, damage: int) -> bool:
        """Check if the attack of self is enough to kill the target

        Args:
            damage (int): the damage taken

        Raises:
            TypeError: if can't access to value

        Returns:
            bool: True if it kill, false if it does not kill
        """

        try:
            if self.health < damage:
                return False
            return True
        except TypeError as e:
            raise TypeError(e)
