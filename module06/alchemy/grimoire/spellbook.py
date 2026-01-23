"""Spellbook helpers for recording spells with validated ingredients.

Provides a single public helper to record a spell after validating
its ingredients.
"""

__all__: list[str] = ["record_spell"]


def record_spell(spell_name: str, ingredients: str) -> str:
    """Record a spell with validated ingredients.

    Args:
        spell_name (str): Name of the spell to record.
        ingredients (str): Ingredients to use for the spell.

    Returns:
        str: Result message indicating if spell was recorded or rejected.
    """
    from .validator import validate_ingredients
    validation: str = validate_ingredients(ingredients)
    if "INVALID" in validation:
        return f"Spell rejected: {spell_name} ({validation})"
    return f"Spell recorded: {spell_name} ({validation})"
