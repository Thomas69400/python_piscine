"""Examples of functools utilities: partial, reduce, lru_cache and
singledispatch.

Includes base enchantment factory, spell reduction helpers, a memoized
Fibonacci, and a singledispatch-based dispatcher factory.
"""
from functools import partial, reduce, lru_cache, singledispatch
import operator
from typing import Dict, List, Any, Callable


def base_enchant(power: int, element: str, target: str) -> Dict[str, Any]:
    """Create a base enchantment dictionary for a target."""
    return {"power": power, "element": element, "target": target}


def spell_reducer(spells: List[int], operation: str) -> int:
    """Reduce a list of integer spell powers by operation.

    Supported operations: "add", "min", "multiply", "max".
    """
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


def partial_enchanter(base_enchantment: Callable[[int, str, str],
                                                 Dict[str, Any]]
                      ) -> Dict[str, Callable[..., Dict[str, Any]]]:
    """Return a mapping of partially applied enchantment factories.

    base_enchantment is expected to accept (power, element, target).
    """
    enchant: Dict[str, Callable[..., Dict[str, Any]]] = {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning")
    }
    return enchant


@lru_cache
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using memoization."""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Return a singledispatch dispatcher that handles int, str and list
    args."""
    @singledispatch
    def dispatcher(arg: Any) -> str:
        return f"Argument type not supported: {type(arg).__name__}"

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"{spell} damage inflict"

    @dispatcher.register(str)
    def _(enchantment: str) -> str:
        return f"{enchantment} applied"

    @dispatcher.register(list)
    def _(spells: list) -> str:
        return "".join([spell + " casted, " for spell in spells]).rstrip(", ")
    return dispatcher


def main() -> None:
    spells: List[str] = ["earthquake", "tsunami", "fireball", "freeze"]
    spell_powers: List[int] = [25, 48, 15, 30, 48, 35]
    operations: List[str] = ['add', 'multiply', 'max', 'min']

    print("Testing spell reducer...")
    try:
        reducer: int = spell_reducer(spell_powers, operations[0])
        print("Sum: ", reducer)
        reducer: int = spell_reducer(spell_powers, operations[1])
        print("Product: ", reducer)
        reducer: int = spell_reducer(spell_powers, operations[2])
        print("Max: ", reducer)
        reducer: int = spell_reducer(spell_powers, operations[3])
        print("Min: ", reducer)
    except TypeError as e:
        print(f"Error spell reducer: {e}")

    print("\nTesting partial enchanter...")
    try:
        enchanter: Dict[str, Callable[..., Dict[str, Any]]
                        ] = partial_enchanter(base_enchant)
        print(enchanter.keys())
        print(f'Fire enchant: {enchanter["fire_enchant"]("Goblin")}')
    except TypeError as e:
        print(f"TypeError partial enchanter: Type = {e}")
    except KeyError as e:
        print(f"KeyError partial enchanter: Key = {e}")

    print("\nTesting memoized fibonacci...")
    try:
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")
    except TypeError as e:
        print(f"Error fibonacci: {e}")

    print("\nTesting spell dispatcher...")
    try:
        dispatcher = spell_dispatcher()
        print(dispatcher(spells))
        print(dispatcher(50))
        print(dispatcher("fire"))
        print(dispatcher({"test": 1}))
    except TypeError as e:
        print(f"Error spell dispatcher: {e}")


if __name__ == "__main__":
    main()
