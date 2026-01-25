from typing import Dict, List, Callable, Any


def mage_counter() -> Callable[[], int]:
    """Return a counter function that increments and returns an integer."""
    i: int = 0

    def count() -> int:
        """Increment the enclosed counter and return the new value."""
        nonlocal i
        i += 1
        return i

    return count


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Return an accumulator that adds subsequent power values."""
    accumulation: int = initial_power

    def accumulator(power: int) -> int:
        """Add power to the accumulated total and return the sum."""
        nonlocal accumulation
        accumulation += power
        return accumulation

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Return a simple enchantment function that prefixes the item name."""
    def enchant(item_name: str) -> str:
        """Apply the enchantment type to the given item name."""
        return enchantment_type + " " + item_name
    return enchant


def memory_vault() -> Dict[str, Callable[..., Any]]:
    """Return a simple in-memory vault with 'store' and 'recall' callables."""
    vault: Dict[str, Any] = dict()

    def store(key: str, value: Any) -> None:
        """Store a value under a string key in the vault."""
        vault.update({key: value})
        return None

    def recall(key: str) -> Any:
        """Return the stored value for key or a not-found message."""
        if key in vault:
            return vault[key]
        return "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:
    initial_powers: List[int] = [66, 24, 65]
    power_additions: List[int] = [18, 12, 10, 12, 19]
    enchantment_types: List[str] = ['Shocking', 'Frozen', 'Earthen']
    items_to_enchant: List[str] = ['Armor', 'Wand', 'Amulet', 'Ring']

    print("Testing mage counter...")
    try:
        counter: Callable[[], int] = mage_counter()
        print(f"Call 1: {counter()}")
        print(f"Call 2: {counter()}")
        print(f"Call 3: {counter()}")
    except TypeError as e:
        print(f"Error mage counter: {e}")

    print("\nTesting spell accumulator...")
    try:
        accumulator: Callable[[int], int] = spell_accumulator(
            initial_powers[0])
        print(f"Accumulated power: {accumulator(power_additions[0])}")
        print(f"Accumulated power: {accumulator(power_additions[2])}")
        print(f"Accumulated power: {accumulator(power_additions[1])}")
    except TypeError as e:
        print(f"Error spell accumulator: {e}")

    print("\nTesting enchantment factory...")
    try:
        shocking: Callable[[str], str] = enchantment_factory(
            enchantment_types[0])
        earthen: Callable[[str], str] = enchantment_factory(
            enchantment_types[2])
        print(shocking(items_to_enchant[0]))
        print(earthen(items_to_enchant[3]))
    except TypeError as e:
        print(f"Error enchantment factory: {e}")

    print("\nTesting memory vault...")
    try:
        vault: Dict[str, Callable[..., Any]] = memory_vault()
        vault["store"]("1", items_to_enchant[0])
        vault["store"]("2", items_to_enchant[1])
        print(vault["recall"]("1"))
        print(vault["recall"]("3"))
        vault2: Dict[str, Callable[..., Any]] = memory_vault()
        print(vault2["recall"]("1"))
    except TypeError as e:
        print(f"Error memory vault: {e}")
    except KeyError as e:
        print(f"Error memory vault, bad key: {e}")


if __name__ == "__main__":
    main()
