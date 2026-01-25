"""Command-line inventory analysis utility.

Parses argv items of the form name:count and prints summaries and suggestions.
"""
import sys
from typing import Dict, List, Tuple


def main() -> None:
    """Execute the inventory analysis from command-line arguments."""

    if len(sys.argv) <= 1:
        print("Usage: python3 ft_inventory_system.py item:count ...")
        return

    inventory: Dict[str, int] = dict()
    for i in range(1, len(sys.argv)):
        try:
            data = sys.argv[i].split(":")
            inventory.update({
                data[0]: int(data[1])
            })
        except ValueError:
            print(f"Invalid format: {sys.argv[i]}")
            return

    print("=== Inventory System Analysis ===")
    total_item: int = 0
    for item in inventory.values():
        total_item += item
    print(f"Total items in inventory: {total_item}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    sort: List[Tuple[str, int]] = sorted(
        inventory.items(), key=lambda x: x[1], reverse=True)
    for item in sort:
        unit_str = "unit" if item[1] == 1 else "units"
        print(f"{item[0]}: {item[1]} {unit_str}"
              + f" ({(item[1]/total_item * 100):.1f}%)")

    print("\n=== Inventory Statistics ===")
    most_abundant_unit_str = "unit" if sort[0][1] == 1 else "units"
    least_abundant_unit_str = "unit" if sort[-1][1] == 1 else "units"
    print(
        f"Most abundant: {sort[0][0]} ({sort[0][1]} {most_abundant_unit_str})")
    print(
        f"Least abundant: {sort[-1][0]} ({sort[-1][1]} "
        f"{least_abundant_unit_str})")

    print("\n=== Item Categories ===")
    moderate: Dict[str, int] = dict()
    scarce: Dict[str, int] = dict()
    for item in inventory:
        if inventory[item] >= 5:
            moderate.update({item: inventory[item]})
        else:
            scarce.update({item: inventory[item]})
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    restock: List[str] = list()
    for item in inventory:
        if inventory[item] == 1:
            restock.append(item)
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    is_sword: bool = "sword" in list(inventory.keys())
    print(f"Sample lookup - 'sword' in inventory: {is_sword}")


if __name__ == "__main__":
    main()
