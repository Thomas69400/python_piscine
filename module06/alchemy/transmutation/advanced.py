def philosophers_stone() -> str:
    """Return a string

    Returns:
        str: string referencing philosopher
    """

    from .basic import lead_to_gold
    from ..potions import healing_potion
    return "Philosopher’s stone created using " + \
        f"{lead_to_gold()} and {healing_potion()}"


def elixir_of_life() -> str:
    """Return a string

    Returns:
        str: string referencing elixir
    """

    return "Elixir of life: eternal youth achieved!"
