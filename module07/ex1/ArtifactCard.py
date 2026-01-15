from typing import Dict, Union
from ex0.Card import Card


class ArtifactCard(Card):
    """A card representing an artifact with durability and special effects.

    Extends the base Card class with artifact mechanics including durability
    points and persistent effects that can be activated during the game.

    Args:
        Card (Card): Parent abstract base class.
    """

    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int, effect: str) -> None:
        """Initialize an ArtifactCard

        Args:
            name (str): name of artifact
            cost (int): cost of artifact
            rarity (str): rarity of artifact
            durability (int): durability of artifact
            effect (str): effect of artifact
        """
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect: str = effect

    def play(self, game_state: dict) -> dict:
        """Play an Artifact

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
                "effect": self.effect
            }
            game_state["mana"] -= self.cost
            return play
        except TypeError as e:
            raise (e)

    def activate_ability(self) -> dict:
        """Activate the ability of the artifact.

        Parses the effect string (formatted as 'duration:effect') and
        returns activation information.

        Raises:
            IndexError: If the effect string is not properly formatted
            with ':'.

        Returns:
            dict: Activation information containing card name, effect
            description, and duration.
        """

        try:
            effect = self.effect.split(":")
            activation = {
                "card_activated": self.name,
                "effect": effect[1],
                "duration": effect[0]
            }
            return activation
        except IndexError as e:
            raise IndexError(e)

    def get_type(self) -> str:
        """Get the type of ArtifactCard

        Returns:
            str: artifact
        """

        return "Artifact"
