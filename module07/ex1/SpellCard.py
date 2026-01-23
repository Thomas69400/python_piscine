from ex0.Card import Card
from typing import Dict, Union, List


class SpellCard(Card):
    """A card representing a spell with various effects.

    Extends the base Card class with spell mechanics including different
    effect types (damage, heal, buff, debuff) that can be applied to targets.

    Args:
        Card (Card): Parent abstract base class.
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

    def play(self,
             game_state: Dict[str, Union[int, str]]) -> Dict[str,
                                                             Union[str,
                                                                   int]]:
        """Play a spell and deduct mana from the game state.

        Args:
            game_state (Dict[str, Union[int, str]]): Mutable game state
            containing 'mana'.

        Returns:
            Dict[str, Union[str, int]]: Summary of the play.
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

    def resolve_effect(self, targets: List[Card]) -> Dict[str,
                                                          Union[str, int]]:
        """Resolve the effect of this spell against the given targets.

        Extracts a numeric value from the effect_type string and applies
        damage/heal/buff/debuff accordingly.

        Args:
            targets (List[Card]): Targets to apply the effect to.

        Returns:
            Dict[str, Union[str, int]]: Summary including card, targets,
            value and effect kind.
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
            raise TypeError(e)

    def get_type(self) -> str:
        """Get the type of SpellCard

        Returns:
            str: spell
        """

        return "Spell"
