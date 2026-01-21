from typing import Dict, List


def mage_counter(start: int = 0) -> callable:
    i: int = start

    def count() -> int:
        nonlocal i
        i += 1
        return i

    return count


def spell_accumulator(initial_power: int) -> callable:
    accumulation: int = initial_power

    def accumulator(power: int = 0) -> int:
        nonlocal accumulation
        accumulation += power
        return accumulation

    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    enchantment: str = enchantment_type

    def enchant(item_name: str) -> str:
        nonlocal enchantment
        return enchantment + " " + item_name
    return enchant


def memory_vault() -> dict[str, callable]:
    vault: Dict[str, callable] = dict()

    def store(key: str, value: str) -> None:
        nonlocal vault
        vault.update({
            key: value
        })
        return

    def recall(key: str) -> str:
        nonlocal vault
        if key in vault:
            return vault[key]
        return "Memory not found"

    return {"store": store, "recall": recall}


def main():
    initial_powers: List[int] = [66, 24, 65]
    power_additions: List[int] = [18, 12, 10, 12, 19]
    enchantment_types: List[str] = ['Shocking', 'Frozen', 'Earthen']
    items_to_enchant: List[str] = ['Armor', 'Wand', 'Amulet', 'Ring']

    print("Testing mage counter...")
    try:
        counter: callable = mage_counter()
        print(f"Call 1: {counter()}")
        print(f"Call 2: {counter()}")
        print(f"Call 3: {counter()}")
    except TypeError as e:
        print(f"Error mage counter: {e}")

    print("\nTesting spell accumulator...")
    try:
        accumulator: callable = spell_accumulator(initial_powers[0])
        print(f"Accumulated power: {accumulator()}")
        print(f"Accumulated power: {accumulator(power_additions[2])}")
        print(f"Accumulated power: {accumulator(power_additions[1])}")
    except TypeError as e:
        print(f"Error spell accumulator: {e}")

    print("\nTesting enchantment factory...")
    try:
        shocking: callable = enchantment_factory(enchantment_types[0])
        earthen: callable = enchantment_factory(enchantment_types[2])
        print(shocking(items_to_enchant[0]))
        print(earthen(items_to_enchant[3]))
    except TypeError as e:
        print(f"Error enchantment factory: {e}")

    print("\nTesting memory vault...")
    try:
        vault: callable = memory_vault()
        vault["store"]("1", items_to_enchant[0])
        vault["store"]("2", items_to_enchant[1])
        print(vault["recall"]("1"))
        print(vault["recall"]("3"))
    except TypeError as e:
        print(f"Error memory vault: {e}")
    except KeyError as e:
        print(f"Error memory vault, bad key: {e}")


if __name__ == "__main__":
    main()
