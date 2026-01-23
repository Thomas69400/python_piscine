"""Examples of different import patterns for the alchemy package."""


def method_1() -> None:
    """Test full module import method."""
    try:
        import alchemy.elements
        print("Method 1 - Full module import:")
        print("alchemy.elements.create_fire(): ", end="")
        result: str = alchemy.elements.create_fire()
        print(result)
    except AttributeError:
        print("AttributeError : no attribute")


def method_2() -> None:
    """Test specific function import method."""
    try:
        from alchemy.elements import create_water
        print("\nMethod 2 - Specific function import:")
        print("create_water(): ", end="")
        result: str = create_water()
        print(result)
    except AttributeError:
        print("AttributeError : no attribute")


def method_3() -> None:
    """Test aliased import method."""
    try:
        from alchemy.potions import healing_potion as heal
        print("\nMethod 3 - Aliased import:")
        print("heal(): ", end="")
        result: str = heal()
        print(result)
    except AttributeError:
        print("AttributeError : no attribute")


def method_4() -> None:
    """Test multiple imports method."""
    try:
        from alchemy.elements import create_earth, create_fire
        from alchemy.potions import strength_potion
        print("\nMethod 4 - Multiple imports:")
        print("create_earth(): ", end="")
        result1: str = create_earth()
        print(result1)
        print("create_fire(): ", end="")
        result2: str = create_fire()
        print(result2)
        print("strength_potion(): ", end="")
        result3: str = strength_potion()
        print(result3)
    except AttributeError:
        print("AttributeError : no attribute")


if __name__ == "__main__":
    print("=== Import Transmutation Mastery ===\n")
    method_1()
    method_2()
    method_3()
    method_4()
    print("\nAll import transmutation methods mastered!")
