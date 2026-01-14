from ex0.Card import Card
from typing import Dict, Union


class SpellCard(Card):
    """Child of Card

    Args:
        Card (Card): Parent
    """

    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        """Initialize a SpellCard

        Args:
            name (str): name of spell
            cost (int): cost of spell
            rarity (str): rarity of spell
            effect_type (str): effect of spell
        """

        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    def play(self, game_state: dict) -> dict:
        """Play a spell

        Args:
            game_state (dict): the actual state of the game

        Raises:
            TypeError: if can't access to value

        Returns:
            dict: a dictionary of the play state
        """

        try:
            play: Dict[str, Union[str, int]] = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect_type
            }
            game_state["mana"] -= self.cost
            return play
        except TypeError as e:
            raise (e)

    def resolve_effect(self, targets: list) -> dict:
        """Resolve the effect of spell

        Args:
            targets (list): a list of Cards

        Raises:
            IndexError: if no value in effect

        Returns:
            dict: resumed information as dict
        """

        try:
            effect = {
                "card_played": self.name,
                "targets": [target.name for target in targets]
            }
            value = [int(s)
                     for s in str.split(self.effect_type) if s.isdigit()][0]
            effect.update({"value": value})
            for target in targets:
                if "damage" in self.effect_type:
                    target.health -= value
                    effect.update({"effect": "damage"})
                elif "heal" in self.effect_type:
                    target.health += value
                    effect.update({"effect": "heal"})
                elif "debuff" in self.effect_type:
                    target.attack -= value
                    effect.update({"effect": "debuff"})
                elif "buff" in self.effect_type:
                    target.attack += value
                    effect.update({"effect": "buff"})
            return effect
        except IndexError as e:
            raise IndexError(e)
        except TypeError as e:
            raise (e)

    def get_type(self) -> str:
        """Get the type of SpellCard

        Returns:
            str: spell
        """

        return "Spell"
