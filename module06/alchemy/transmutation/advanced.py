"""Advanced transmutation helpers (philosopher's stone, elixirs)."""

__all__: list[str] = ["philosophers_stone", "elixir_of_life"]


def philosophers_stone() -> str:
    """Create a philosopher's stone using transmutation and potions.

    Returns:
        str: Description of the philosopher's stone creation.
    """
    from .basic import lead_to_gold
    from ..potions import healing_potion
    gold: str = lead_to_gold()
    potion: str = healing_potion()
    return "Philosopher's stone created using " + \
        f"{gold} and {potion}"


def elixir_of_life() -> str:
    """Create the elixir of life for eternal youth.

    Returns:
        str: Description of the elixir of life creation.
    """
    return "Elixir of life: eternal youth achieved!"
