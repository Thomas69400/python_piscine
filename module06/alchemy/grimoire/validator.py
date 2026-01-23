"""Validator utilities for grimoire ingredients.

This module exposes helpers to validate ingredient strings used by spells.
"""

__all__: list[str] = ["validate_ingredients"]


def validate_ingredients(ingredients: str) -> str:
    """Validate if ingredients contain allowed elements.

    Args:
        ingredients (str): The ingredient string to validate.

    Returns:
        str: Validation result with status (VALID or INVALID).
    """
    allowed: list[str] = ["fire", "water", "earth", "air"]
    words: list[str] = ingredients.split()
    if any(word in allowed for word in words):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
