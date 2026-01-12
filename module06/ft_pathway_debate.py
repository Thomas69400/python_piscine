def absolute() -> None:
    """Test absolute import"""

    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    try:
        print("Testing Absolute Imports (from basic.py):")
        print("lead_to_gold(): ", end="")
        print(lead_to_gold())
        print("stone_to_gem(): ", end="")
        print(stone_to_gem())
    except AttributeError:
        print("AttributeError : no attribute")


def relative() -> None:
    """Test relative import"""

    from alchemy.transmutation.advanced import philosophers_stone, \
        elixir_of_life
    try:
        print("\nTesting Relative Imports (from advanced.py):")
        print("philosophers_stone(): ", end="")
        print(philosophers_stone())
        print("elixir_of_life(): ", end="")
        print(elixir_of_life())
    except AttributeError:
        print("AttributeError : no attribute")


def package() -> None:
    """Test import as a package"""

    try:
        import alchemy
        print("\nTesting Package Access:")
        print("alchemy.transmutation.lead_to_gold(): ", end="")
        print(alchemy.transmutation.lead_to_gold())
        print("alchemy.transmutation.philosophers_stone(): ", end="")
        print(alchemy.transmutation.philosophers_stone())
    except AttributeError:
        print("AttributeError : no attribute")


if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===\n")
    absolute()
    relative()
    package()
    print("\nBoth pathways work! Absolute: clear, Relative: concise")
