from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:")

    state = {"mana": 6}
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("\nCreatureCard Info:")
    print(dragon.get_card_info())

    print(f"\nPlaying Fire Dragon with {state['mana']} mana available:")
    playable = dragon.is_playable(state['mana'])
    print(f"Playable: {playable}")
    if playable:
        print(f"Play result: {dragon.play(state)}")

    print("\nFire Dragon attacks Goblin Warrior:")
    goblin = CreatureCard("Goblin Warrior", 3, "Rare", 4, 5)
    print(f"Attack result: {dragon.attack_target(goblin)}")

    state["mana"] = 3
    print(f"\nTesting insufficient mana ({state['mana']} available):")
    print(f"Playable: {dragon.is_playable(state['mana'])}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
