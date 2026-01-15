

def healing_potion() -> str:
    """Brew a healing potion using fire and water elements.

    Returns:
        str: Description of the healing potion creation.
    """
    from .elements import create_fire, create_water
    fire: str = create_fire()
    water: str = create_water()
    return "Healing potion brewed with " + \
        f"{fire} and " + \
        f"{water}"


def strength_potion() -> str:
    """Brew a strength potion using fire and earth elements.

    Returns:
        str: Description of the strength potion creation.
    """
    from .elements import create_fire, create_earth
    earth: str = create_earth()
    fire: str = create_fire()
    return "Strength potion brewed with " + \
        f"{earth} and " + \
        f"{fire}"


def invisibility_potion() -> str:
    """Brew an invisibility potion using air and water elements.

    Returns:
        str: Description of the invisibility potion creation.
    """
    from .elements import create_air, create_water
    air: str = create_air()
    water: str = create_water()
    return "Invisibility potion brewed with " + \
        f"{air} and " + \
        f"{water}"


def wisdom_potion() -> str:
    """Brew a wisdom potion using all four elements.

    Returns:
        str: Description of the wisdom potion creation.
    """
    from .elements import create_air, create_water, create_fire, create_earth
    fire: str = create_fire()
    water: str = create_water()
    earth: str = create_earth()
    air: str = create_air()
    return "Wisdom potion brewed with all elements: " + \
        fire + " " + \
        water + " " + \
        earth + " " + \
        air
