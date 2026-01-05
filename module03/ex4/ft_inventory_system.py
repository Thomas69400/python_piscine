class Player():
    """Class Player, it has a name and an inventory"""

    def __init__(self, name: str) -> None:
        """Initialize a Player

        Args:
            name (str): name of Player
        """

        self.name = name
        self.inventory = dict()

    def add_item(self, item: dict) -> None:
        """Add an item to inventory of player

        Args:
            item (dict): the item to add to inventory
        """

        self.inventory.update(item)

    def get_invent(self) -> dict:
        """Get the inventory of player

        Returns:
            dict: the inventory of player
        """

        return self.inventory

    def show_inventory(self) -> None:
        """Print the inventory"""

        print(f"=== {self.name}'s Inventory ===")
        for item in self.inventory:
            print(f"{item} ", end="")
            total = self.inventory[item]["nbr"] * self.inventory[item]["value"]
            print(f"({self.inventory[item]['cate']}, "
                  f"{self.inventory[item]['rare']}): " +
                  f"{self.inventory[item]['nbr']}x @ " +
                  f"{self.inventory[item]['value']} " +
                  f"gold each = {total} gold")

    def get_invent_value(self) -> int:
        """Get the total value of the inventory

        Returns:
            int: the total value of the inventory
        """

        tot = 0
        for item in self.inventory:
            tot += self.inventory[item]["nbr"] * self.inventory[item]["value"]
        return tot

    def get_invent_count(self) -> int:
        """Get the number of item in inventory

        Returns:
            int: the number of item in inventory
        """

        tot = 0
        for item in self.inventory:
            tot += self.inventory[item]["nbr"]
        return tot

    def get_invent_cate(self) -> int:
        """Get the number of each categories the item belongs

        Returns:
            int: the numbers of each categories
        """

        weapon = 0
        cons = 0
        arm = 0
        for item in self.inventory:
            if self.inventory[item]["cate"] == "weapon":
                weapon += self.inventory[item]["nbr"]
            if self.inventory[item]["cate"] == "consumable":
                cons += self.inventory[item]["nbr"]
            if self.inventory[item]["cate"] == "armor":
                arm += self.inventory[item]["nbr"]
        return weapon, cons, arm

    @staticmethod
    def transfer_item(inv_from: dict, inv_to: dict, item_name: str,
                      nbr: int) -> None:
        """Transfer an item from an inventory to an other

        Args:
            inv_from (dict): the inventory that give the item
            inv_to (dict): the inventory that receive the item
            item (str): the name of item to give
            nbr (int): the number of item to give
        """

        if item_name in inv_from:
            if inv_from[item_name]["nbr"] < nbr:
                print(
                    f"Not enough {item_name}. Can\'t give {nbr}, "
                    f"only have {inv_from[item_name]['nbr']}")
                return
            inv_to.update({item_name: {"cate": inv_from[item_name]["cate"],
                                       "rare": inv_from[item_name]["rare"],
                                       "nbr": nbr,
                                       "value": inv_from[item_name]["value"]}})
            inv_from[item_name]["nbr"] -= nbr
            print("Transaction successful!")
        else:
            print(f"Doesn't have the item {item_name} to give.")

    def get_rarest_item(self) -> str:
        """Get the name of the rarest item in inventories

        Returns:
            str: the name of the rarest item
        """

        most = 0
        name = ""
        for item in self.inventory:
            if self.inventory[item]["value"] > most:
                most = self.inventory[item]["value"]
                name = item
        return name


def analytics(inv1: Player, inv2: Player) -> None:
    """Give details on inventory between 2 Players

    Args:
        inv1 (Player): first Player
        inv2 (Player): second Player
    """
    if inv1.get_invent_value() > inv2.get_invent_value():
        print(f"Most valuable player: {inv1.name} " +
              f"({inv1.get_invent_value()} gold)")
    if inv1.get_invent_count() > inv2.get_invent_count():
        print(f"Most items: {inv1.name} " +
              f"({inv1.get_invent_count()} items)")
    print(f"Rarest items: {inv1.get_rarest_item()}, {inv2.get_rarest_item()}")


if __name__ == "__main__":
    print("=== Player Inventory System ===\n")
    alice = Player("Alice")
    bob = Player("Bob")
    alice.add_item({"sword": {"cate": "weapon", "rare": "rare",
                              "nbr": 1, "value": 500}})
    alice.add_item({"potion": {"cate": "consumable", "rare": "common",
                               "nbr": 5, "value":  50}})
    alice.add_item({"shield": {"cate": "armor", "rare": "uncommon",
                   "nbr": 1, "value": 200}})
    bob.add_item({"magic_ring": {"cate": "armor", "rare": "rare",
                                 "nbr": 1, "value": 500}})

    alice.show_inventory()
    print(f"\nInventory value: {alice.get_invent_value()} gold")
    print(f"Item count: {alice.get_invent_count()} items")
    weapon, cons, arm = alice.get_invent_cate()
    print(f"Categories: weapon({weapon}), consumable({cons}), armor({arm})")

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    Player.transfer_item(alice.get_invent(), bob.get_invent(), "potion", 2)
    print("\n=== Updated Inventories ===")
    alice.show_inventory()
    bob.show_inventory()

    print("\n=== Inventory Analytics ===")
    analytics(alice, bob)
