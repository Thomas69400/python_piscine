"""Basic transmutation functions using elemental helpers."""
__all__: list[str] = ["lead_to_gold", "stone_to_gem"]

from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """Transmute lead into gold using fire element.

    Returns:
        str: Description of the lead to gold transmutation.
    """
    fire_element: str = create_fire()
    return f"Lead transmuted to gold using {fire_element}"


def stone_to_gem() -> str:
    """Transmute stone into gem using earth element.

    Returns:
        str: Description of the stone to gem transmutation.
    """
    earth_element: str = create_earth()
    return f"Stone transmuted to gem using {earth_element}"
