"""Print formatted seed inventory lines for various unit types."""


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    """Print a formatted inventory line for a seed type.

    Args:
        seed_type (str): The seed variety name.
        quantity (int): The quantity of the seed in the provided unit.
        unit (str): The unit type, e.g. "packets", "grams", or "area".
    """

    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(f"{seed_type.capitalize()} seeds: covers {quantity} square "
              + "meters")
    else:
        print(f"{seed_type.capitalize()} seeds: {quantity} Unknown unit type")
