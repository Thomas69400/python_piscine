from functools import partial, reduce, lru_cache, singledispatch
import operator
from typing import Dict


def base_enchant(power: int, element: str, target: str) -> dict:
    return {"power": power, "element": element, "target": target}


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        reduced = reduce(operator.add, spells)
    elif operation == "min":
        reduced = reduce(min, spells)
    elif operation == "multiply":
        reduced = reduce(operator.mul, spells)
    elif operation == "max":
        reduced = reduce(max, spells)
    else:
        raise TypeError(f"operation unknown: {operation}")
    return reduced


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    enchant: Dict[str, callable] = {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50,
                                     "lightning")
    }
    return enchant


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@singledispatch
def spell_dispatcher() -> callable:
    pass


def main():
    spell_powers = [25, 48, 15, 30, 48, 35]
    operations = ['add', 'multiply', 'max', 'min']

    print("Testing spell reducer...")
    try:
        reducer: int = spell_reducer(spell_powers, operations[0])
        print("Sum: ", reducer)
        reducer: int = spell_reducer(spell_powers, operations[1])
        print("Product: ", reducer)
        reducer: int = spell_reducer(spell_powers, operations[2])
        print("Min: ", reducer)
        reducer: int = spell_reducer(spell_powers, operations[3])
        print("Max: ", reducer)
    except TypeError as e:
        print(f"Error spell reducer: {e}")

    print("\nTesting partial enchanter...")
    try:
        enchanter: Dict[str, callable] = partial_enchanter(base_enchant)
        print(enchanter.keys())
        print(f'Fire enchant: {enchanter["fire_enchant"]("Goblin")}')
    except TypeError as e:
        print(f"TypeError partial enchanter: Type = {e}")
    except KeyError as e:
        print(f"KeyError partial enchanter: Key = {e}")

    print("\nTesting memoized fibonacci...")
    try:
        print(f"Fib (10): {memoized_fibonacci(10)}")
        print(f"Fib (15): {memoized_fibonacci(15)}")
    except TypeError as e:
        print(f"Error fibonacci: {e}")

    print("\nTesting spell dispatcher...")
    try:
        dispatcher = spell_dispatcher()
    except TypeError as e:
        print(f"Error spell dispatcher: {e}")


if __name__ == "__main__":
    main()
