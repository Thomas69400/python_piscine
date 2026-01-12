def ingredient() -> None:
    """Test function validate_ingredient()"""

    from alchemy.grimoire.validator import validate_ingredients

    try:
        print("\nTesting ingredient validation:")
        print("validate_ingredients(\"fire air\"): ", end="")
        print(validate_ingredients("fire air"))
        print("validate_ingredients(\"dragon scales\"): ", end="")
        print(validate_ingredients("dragon scales"))
    except AttributeError:
        print("AttributeError: no attribute")


def spell() -> None:
    """Test function record_spell()"""

    from alchemy.grimoire.spellbook import record_spell

    try:
        print("\nTesting spell recording with validation:")
        print("record_spell(\"Fireball\", \"fire air\"): ", end="")
        print(record_spell("Fireball", "fire air"))
        print("record_spell(\"Dark Magic\", \"shadow\"): ", end="")
        print(record_spell("Dark Magic", "shadow"))
    except AttributeError:
        print("AttributeError: no attribute")


def late() -> None:
    """Test late import"""

    from alchemy.grimoire.spellbook import record_spell

    try:
        print("\nTesting late import technique:")
        print("record_spell(\"Lightning\", \"air\"): ", end="")
        print(record_spell("Lightning", "air"))
    except AttributeError:
        print("AttributeError: no attribute")


if __name__ == "__main__":
    print("=== Circular Curse Breaking ===")

    ingredient()
    spell()
    late()
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
