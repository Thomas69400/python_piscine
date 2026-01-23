"""Demonstrate late imports to avoid circular dependencies in the grimoire."""


def ingredient() -> None:
    """Test the validate_ingredients function."""
    from alchemy.grimoire.validator import validate_ingredients

    try:
        print("\nTesting ingredient validation:")
        print("validate_ingredients(\"fire air\"): ", end="")
        result1: str = validate_ingredients("fire air")
        print(result1)
        print("validate_ingredients(\"dragon scales\"): ", end="")
        result2: str = validate_ingredients("dragon scales")
        print(result2)
    except AttributeError:
        print("AttributeError: no attribute")


def spell() -> None:
    """Test the record_spell function."""
    from alchemy.grimoire.spellbook import record_spell

    try:
        print("\nTesting spell recording with validation:")
        print("record_spell(\"Fireball\", \"fire air\"): ", end="")
        result1: str = record_spell("Fireball", "fire air")
        print(result1)
        print("record_spell(\"Dark Magic\", \"shadow\"): ", end="")
        result2: str = record_spell("Dark Magic", "shadow")
        print(result2)
    except AttributeError:
        print("AttributeError: no attribute")


def late() -> None:
    """Test late import technique to avoid circular dependencies."""
    from alchemy.grimoire.spellbook import record_spell

    try:
        print("\nTesting late import technique:")
        print("record_spell(\"Lightning\", \"air\"): ", end="")
        result: str = record_spell("Lightning", "air")
        print(result)
    except AttributeError:
        print("AttributeError: no attribute")


if __name__ == "__main__":
    print("=== Circular Curse Breaking ===")

    ingredient()
    spell()
    late()
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
