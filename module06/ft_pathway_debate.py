"""Demonstrate different import styles: absolute, relative and package-level.

This script attempts to import and call functions from the alchemy.
transmutation package using different import approaches.
"""


def absolute() -> None:
    """Test absolute import method."""
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    try:
        print("Testing Absolute Imports (from basic.py):")
        print("lead_to_gold(): ", end="")
        result1: str = lead_to_gold()
        print(result1)
        print("stone_to_gem(): ", end="")
        result2: str = stone_to_gem()
        print(result2)
    except AttributeError:
        print("AttributeError : no attribute")


def relative() -> None:
    """Test relative import method."""
    from alchemy.transmutation.advanced import philosophers_stone, \
        elixir_of_life
    try:
        print("\nTesting Relative Imports (from advanced.py):")
        print("philosophers_stone(): ", end="")
        result1: str = philosophers_stone()
        print(result1)
        print("elixir_of_life(): ", end="")
        result2: str = elixir_of_life()
        print(result2)
    except AttributeError:
        print("AttributeError : no attribute")


def package() -> None:
    """Test package-level import method."""
    try:
        import alchemy
        print("\nTesting Package Access:")
        print("alchemy.transmutation.lead_to_gold(): ", end="")
        result1: str = alchemy.transmutation.lead_to_gold()
        print(result1)
        print("alchemy.transmutation.philosophers_stone(): ", end="")
        result2: str = alchemy.transmutation.philosophers_stone()
        print(result2)
    except AttributeError:
        print("AttributeError : no attribute")


if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===\n")
    absolute()
    relative()
    package()
    print("\nBoth pathways work! Absolute: clear, Relative: concise")
