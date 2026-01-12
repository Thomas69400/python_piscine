def validate_ingredients(ingredients: str) -> str:
    """Return a string

    Args:
        ingredients (str): the ingredient to check

    Returns:
        str: Valid if ingredient is valid else invalid
    """

    if "fire" or "water" or "earth" or "air" in ingredients:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
