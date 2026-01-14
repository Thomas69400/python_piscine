def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    """Print the seed in inventory

    Args:
        seed_type (str): the type of the seed
        quantity (int): the number of seed
        unit (str): the unit of seed
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
