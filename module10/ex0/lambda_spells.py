from typing import List, Dict, Union


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    try:
        sort: List[dict] = sorted(artifacts,
                                  key=lambda a: a["power"], reverse=True)
        return sort
    except KeyError as e:
        raise KeyError(e)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    try:
        sort: List[dict] = list(
            filter(lambda m: m["power"] >= min_power, mages))
        return sort
    except KeyError as e:
        raise KeyError(e)
    except TypeError as e:
        raise TypeError(f"Min power = '{min_power}', {e}")


def spell_transformer(spells: list[str]) -> list[str]:
    try:
        sort: List[str] = list(map(lambda s: '* ' + s + ' *', spells))
        return sort
    except TypeError as e:
        raise TypeError(f"Spells = {spells}. {e}")


def mage_stats(mages: list[dict]) -> dict:
    try:
        sort: Dict[str, Union[int, float]] = {
            "max_power": max(mages, key=lambda m: m["power"])["power"],
            "min_power": min(mages, key=lambda m: m["power"])["power"],
            "avg_power": sum([mage["power"] for mage in mages]) / len(mages)
        }
        return sort
    except KeyError as e:
        raise KeyError(e)
    except TypeError as e:
        raise TypeError(e)


def main():
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
        print(artifact_sorter(artifacts))
    except KeyError as e:
        print(f"Error artifact sorter : {e}")

    print("\nTesting power filter...")
    try:
        print(power_filter(mages, 80))
    except (KeyError, TypeError) as e:
        print(f"Error power filter : {e}")

    print("\nTesting spell transformer...")
    try:
        print(spell_transformer(spells))
    except TypeError as e:
        print(f"Error spell transformer : {e}")

    print("\nTesting mage statistics...")
    try:
        print(mage_stats(mages))
    except (KeyError, TypeError) as e:
        print(f"Error mages statistics : {e}")


if __name__ == "__main__":
    main()
