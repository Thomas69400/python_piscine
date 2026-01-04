if __name__ == "__main__":
    print("=== Player Inventory System ===\n")
    players = dict(alice={dict(name="sword", cat="weapon", rare="rare",
                          nbr=1, gold=500),
                          dict(name="potion", cat="consumable", rare="common",
                          nbr=5, gold=50),
                          dict(name="shield", cat="armor", rare="uncommon",
                          nbr=1, gold=200)},
                   bob=[dict(name="magic_ring", cat="armor", rare="rare",
                        nbr=1, gold=500)])
    print("=== Alice's Inventory ===")
    tot = 0
    n = 0
    weap = 0
    cons = 0
    arm = 0
    for item in players.get("alice"):
        print(f"{item.get("name")} ({item.get("cat")}, {item.get("rare")}):" +
              f" {item.get("nbr")}x @ {item.get("gold")}" +
              f" each = {item.get("nbr") * item.get("gold")} gold")
        tot += item.get("nbr") * item.get("gold")
        n += item.get("nbr")
        if item.get("cat") == "weapon":
            weap += item.get("nbr")
        elif item.get("cat") == "consumable":
            cons += item.get("nbr")
        elif item.get("cat") == "armor":
            arm += item.get("nbr")
    print(f"\nInventory value: {tot} gold")
    print(f"Item count: {n} items")
    print(f"Categories: weapon({weap}), consumable({cons}), armor({arm})")

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    a = players["alice"]
    print("Transaction successful!")
