def method_1() -> None:
    try:
        import alchemy
        print("Method 1 - Full module import:")
        print("alchemy.elements.create_fire(): ", end="")
        print(alchemy.elements.create_fire())
    except AttributeError:
        print("AttributeError : no attribute")


def method_2() -> None:
    try:
        from alchemy.elements import create_water
        print("\nMethod 2 - Specific function import:")
        print("create_water(): ", end="")
        print(create_water())
    except AttributeError:
        print("AttributeError : no attribute")


def method_3() -> None:
    try:
        from alchemy.potions import healing_potion as heal
        print("\nMethod 3 - Aliased import:")
        print("heal(): ", end="")
        print(heal())
    except AttributeError:
        print("AttributeError : no attribute")


def method_4() -> None:
    try:
        from alchemy.elements import create_earth, create_fire
        from alchemy.potions import strength_potion
        print("\nMethod 4 - Multiple imports:")
        print("create_earth(): ", end="")
        print(create_earth())
        print("create_fire(): ", end="")
        print(create_fire())
        print("strength_potion(): ", end="")
        print(strength_potion())
    except AttributeError:
        print("AttributeError : no attribute")


if __name__ == "__main__":
    print("=== Import Transmutation Mastery ===\n")
    method_1()
    method_2()
    method_3()
    method_4()
    print("\nAll import transmutation methods mastered!")
