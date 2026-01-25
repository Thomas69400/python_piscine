from typing import List, Callable, Any, Tuple


def fireball(target: str) -> str:
    """Return a string describing a fireball hitting the target."""
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    """Return a string describing a heal applied to the target."""
    return f"Heals {target}"


def lightning(damage: int) -> int:
    """Return the integer damage value from a lightning spell."""
    return damage


def ft_condition(name: str) -> bool:
    """Return True when the provided name satisfies a condition."""
    return "Dragon" in name


def spell_combiner(spell1: Callable[[str], Any],
                   spell2: Callable[[str], Any]
                   ) -> Callable[[str], Tuple[Any, Any]]:
    """Combine two single-argument spells into one that returns a tuple."""
    return lambda s: (spell1(s), spell2(s))


def power_amplifier(base_spell: Callable[[int], int],
                    multiplier: int) -> Callable[[int], int]:
    """Return a new spell that amplifies the base spell's integer result."""
    return lambda s: base_spell(s) * multiplier


def conditional_caster(condition: Callable[[str], bool],
                       spell: Callable[[str], Any]
                       ) -> Callable[[str], Any]:
    """Return a caster that only calls spell if condition is True."""
    return lambda x: spell(x) if condition(x) else "Spell fizzled"


def spell_sequence(spells: List[Callable[[str], Any]]
                   ) -> Callable[[str], List[Any]]:
    """Return a function that runs a sequence of spells and collects results.
    """
    return lambda x: [spell(x) for spell in spells]


def main() -> None:

    test_targets: List[str] = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("Testing spell combiner...")
    try:
        combined: Callable[[str], Tuple[Any, Any]
                           ] = spell_combiner(fireball, heal)
        combined_spell: tuple = combined(test_targets[0])
        print(
            f"Combined spell result: {combined_spell[0]}, {combined_spell[1]}")
    except IndexError as e:
        print(f"Error spell combiner: {e}")
    except TypeError as e:
        print(f"Error spell combiner: {e}")

    print("\nTesting power amplifier...")
    try:
        mega_fireball: Callable[[int], int] = power_amplifier(lightning, 3)
        print(f"Original: {lightning(10)}, Amplified: {mega_fireball(10)}")
    except TypeError as e:
        print(f"Error power amplifier: {e}")

    print("\nTesting conditional caster...")
    try:
        condition: Callable[[str], Any] = conditional_caster(
            ft_condition, heal)
        if callable(condition):
            print(condition(test_targets[0]))
        else:
            print(condition)
    except TypeError as e:
        print(f"Error conditional caster: {e}")

    print("\nTesting spell sequence...")
    try:
        spells: Callable[[str], List[Any]] = spell_sequence([fireball, heal])
        print(spells(test_targets[1]))
    except TypeError as e:
        print(f"Error spell sequence: {e}")


if __name__ == "__main__":
    main()
