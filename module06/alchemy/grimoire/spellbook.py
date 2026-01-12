def record_spell(spell_name: str, ingredients: str) -> str:
    """Return a string

    Args:
        spell_name (str): name of the spell
        ingredients (str): name of the ingredient

    Returns:
        str: if spell is recorded or rejected
    """

    from .validator import validate_ingredients
    validation = validate_ingredients(ingredients)
    if "INVALID" in validation:
        return f"Spell rejected: : {spell_name} ({validation})"
    return f"Spell recorded: {spell_name} ({validation})"
