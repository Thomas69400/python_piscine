from typing import List


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals hits {target}"


def lightning(damage: int) -> int:
    return damage


def ft_condition(name: str) -> bool:
    return "Dragon" in name


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda s: (spell1(s), spell2(s))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda s: base_spell(s) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda x: spell(x) if condition(x) else "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    return lambda x: [spell(x) for spell in spells]


def main():

    test_targets: List[str] = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("Testing spell combiner...")
    try:
        combined: callable = spell_combiner(fireball, heal)
        combined_spell: tuple = combined(test_targets[0])
        print(
            f"Combined spell result: {combined_spell[0]}, {combined_spell[1]}")
    except IndexError as e:
        print(f"Error spell combiner: {e}")
    except TypeError as e:
        print(f"Error spell combiner: {e}")

    print("\nTesting power amplifier...")
    try:
        mega_fireball: callable = power_amplifier(lightning, 3)
        print(f"Original: {lightning(10)}, Amplified: {mega_fireball(10)}")
    except TypeError as e:
        print(f"Error power amplifier: {e}")

    print("\nTesting conditional caster...")
    try:
        condition: callable = conditional_caster(ft_condition, heal)
        if callable(condition):
            print(condition(test_targets[0]))
        else:
            print(condition)
    except TypeError as e:
        print(f"Error conditional caster: {e}")

    print("\nTesting spell sequence...")
    try:
        spells: callable = spell_sequence([fireball, heal])
        print(spells(test_targets[1]))
    except TypeError as e:
        print(f"Error spell sequence: {e}")


if __name__ == "__main__":
    main()
