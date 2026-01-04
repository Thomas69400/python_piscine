if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    alice = set(('first_kill', 'level_10', 'treasure_hunter', 'speed_demon'))
    bob = set(('first_kill', 'level_10', 'boss_slayer', 'collector'))
    charlie = set(('level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
                   'perfectionist'))
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    unique = set.union(bob, charlie, alice)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")
    common = set.intersection(bob, charlie, alice)
    print(f"\nCommon to all players: {common}")
    dif = set.difference(bob, charlie, alice)
    dif = dif.union(set.difference(charlie, alice, bob))
    dif = dif.union(set.difference(alice, bob, charlie))
    print(f"Rare achievements (1 player): {dif}")

    print(f"\nAlice vs Bob common: {set.intersection(alice, bob)}")
    print(f"Alice unique: {set.difference(alice, bob)}")
    print(f"Bob unique: {set.difference(bob, alice)}")
