

def healing_potion() -> str:
    from .elements import create_fire, create_water
    return "Healing potion brewed with " + \
        f"{create_fire()} and " + \
        f"{create_water()}"


def strength_potion() -> str:
    from .elements import create_fire, create_earth
    return "Strength potion brewed with " + \
        f"{create_earth()} and " + \
        f"{create_fire()}"


def invisibility_potion() -> str:
    from .elements import create_air, create_water
    return "Invisibility potion brewed with " + \
        f"{create_air()} and " + \
        f"{create_water()}"


def wisdom_potion() -> str:
    from .elements import create_air, create_water, create_fire, create_earth
    return "Wisdom potion brewed with all elements: " + \
        create_fire() + \
        create_water() + \
        create_earth() + \
        create_air()
