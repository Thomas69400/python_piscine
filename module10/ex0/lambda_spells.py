"""Small helpers demonstrating lambda usage: sorting, filtering and mapping.

Functions operate on simple artifact / mage / spell data structures and return
typed collections.
"""

from typing import List, Dict, Union, Any


def artifact_sorter(artifacts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return artifacts sorted by descending 'power' key."""
    sort: List[Dict[str, Any]] = sorted(
        artifacts, key=lambda a: a["power"], reverse=True
    )
    return sort


def power_filter(mages: List[Dict[str, Any]], min_power: int
                 ) -> List[Dict[str, Any]]:
    """Filter mages and return those with power >= min_power."""
    filtered: List[Dict[str, Any]] = list(
        filter(lambda m: m["power"] >= min_power, mages)
    )
    return filtered


def spell_transformer(spells: List[str]) -> List[str]:
    """Return a transformed list of spell names with decorative markers."""
    sort: List[str] = list(map(lambda s: "* " + s + " *", spells))
    return sort


def mage_stats(mages: List[Dict[str, Any]]) -> Dict[str, Union[int, float]]:
    """Compute simple statistics (max, min, avg) for mage power."""
    sort: Dict[str, Union[int, float]] = {
        "max_power": max(mages, key=lambda m: m["power"])["power"],
        "min_power": min(mages, key=lambda m: m["power"])["power"],
        "avg_power": round(
            sum(map(lambda m: m["power"], mages)) / len(mages), 2
        )
    }
    return sort


def main() -> None:
    artifacts = [
        {"name": "Storm Crown", "power": 75, "type": "accessory"},
        {"name": "Ice Wand", "power": 68, "type": "relic"},
        {"name": "Ice Wand", "power": 108, "type": "relic"},
        {"name": "Earth Shield", "power": 107, "type": "accessory"}
    ]

    mages = [
        {"name": "Ash", "power": 83, "element": "water"},
        {"name": "Rowan", "power": 67, "element": "lightning"},
        {"name": "River", "power": 73, "element": "earth"},
        {"name": "Luna", "power": 90, "element": "water"},
        {"name": "Riley", "power": 100, "element": "earth"},
    ]
    spells = ["earthquake", "tsunami", "fireball", "freeze"]

    print("Testing artifact sorter...")
    try:
        sorted_artifacts: List[Dict[str, Any]] = artifact_sorter(artifacts)
        print(f"{sorted_artifacts[0]['name']} "
              f"({sorted_artifacts[0]['power']} power) "
              f"comes before {sorted_artifacts[1]['name']} "
              f"({sorted_artifacts[1]['power']} power)")
    except KeyError as e:
        print(f"Error artifact sorter : {e}")

    print("\nTesting power filter...")
    try:
        power: List[Dict[str, Any]] = power_filter(mages, 80)
        for p in power:
            print(p, end="")
    except (KeyError, TypeError) as e:
        print(f"Error power filter : {e}")

    print("\n\nTesting spell transformer...")
    try:
        transformed: List[str] = spell_transformer(spells)
        print(" ".join(transformed))
    except TypeError as e:
        print(f"Error spell transformer : {e}")

    print("\nTesting mage statistics...")
    try:
        print(mage_stats(mages))
    except (KeyError, TypeError, ZeroDivisionError) as e:
        print(f"Error mages statistics : {e}")


if __name__ == "__main__":
    main()
