from ex2.EliteCard import EliteCard
from ex2.Magical import Magical
from ex2.Combatable import Combatable
from ex0.Card import Card


def main():
    """Execute program"""

    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    methods = [
        method for method
        in dir(EliteCard)
        if callable(getattr(EliteCard, method))
        and not method.startswith('__')
    ]
    card_met = [method for method in methods if hasattr(Card, method)]
    combatable_met = [
        method for method in methods if hasattr(Combatable, method)]
    magical_met = [method for method in methods if hasattr(Magical, method)]
    print(f"- Card: {card_met}")
    print(f"- Combatable: {combatable_met}")
    print(f"- Magical: {magical_met}")

    elite = EliteCard("Arcane Warrior", 8, "Legendary", "melee", 10, 6, 2, 2)
    enemy1 = EliteCard("Enemy1", 3, "Common", "melee", 7, 4, 2, 2)
    enemy2 = EliteCard("Enemy2", 3, "Common", "melee", 7, 4, 2, 2)
    print("\nPlaying Arcane Warrior (Elite Card):\n")

    print("Combat phase:")
    try:
        print(f"Attack result: {elite.attack(enemy1)}")
        print(f"Defense result: {elite.defend(enemy1.damage)}")
    except TypeError as e:
        print(e)

    print("\nMagic phase:")
    try:
        print(f"Spell cast: {elite.cast_spell('Fireball', [enemy1, enemy2])}")
        print(f"Mana channel: {elite.channel_mana(3)}")
    except TypeError as e:
        print(e)

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
