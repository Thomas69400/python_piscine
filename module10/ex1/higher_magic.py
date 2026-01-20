from typing import List


def fireball(names: List[str]) -> str:
    try:
        return [n for n in names if n == "fireball"][0]
    except IndexError as e:
        raise IndexError(e)


def heal(names: List[str]) -> str:
    try:
        return [n for n in names if n == "heal"][0]
    except IndexError as e:
        raise IndexError(e)


def lightning(damage: int) -> int:
    return damage


def ft_condition(name: str) -> bool:
    if name == "fireball":
        return True
    return False


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    try:
        return lambda s: (spell1(s), spell2(s))
    except TypeError as e:
        raise TypeError(e)


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    try:
        return lambda s: base_spell(s) * multiplier
    except ValueError as e:
        raise ValueError(e)


def conditional_caster(condition: callable, spell: callable) -> callable:
    if lambda x: condition(x):
        return lambda x: f"{spell(x)} casted"
    return "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    pass


def main():

    test_spells = ['fireball', 'heal', 'darkness', 'meteor']

    print("Testing spell combiner...")
    try:
        combined: callable = spell_combiner(fireball, heal)
        combined_spell: tuple = combined(test_spells)
        print(
            f"Combined spell result: {combined_spell[0]}, {combined_spell[1]}")
    except IndexError as e:
        print(f"Error spell combiner: {e}")
    except TypeError as e:
        print(f"Error spell combiner: {e}")

    print("\nTesting power amplifier...")
    try:
        mega_fireball = power_amplifier(lightning, 3)
        print(f"Original: {lightning(10)}, Amplified: {mega_fireball(10)}")
    except Exception as e:
        print(f"Error power amplifier: {e}")

    print("\nTesting conditional caster...")
    try:
        condi = conditional_caster(ft_condition, heal)
        if callable(condi):
            print(condi(test_spells))
        else:
            print(condi)
    except Exception as e:
        print(f"Error conditional caster: {e}")


if __name__ == "__main__":
    main()
