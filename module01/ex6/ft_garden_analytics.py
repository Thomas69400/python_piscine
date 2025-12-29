#!/usr/bin/env python3


class Plant:
    """Define all information about a plant"""

    def __init__(self, name: str, height: int) -> None:
        """Create a plant and define her attributes"""

        self.name = name
        self.__height = height
        self.__growth = 0

    def set_height(self, new_height: int) -> None:
        """Set the height of the plant can't be negative"""

        if new_height < 0:
            print(
                f"Invalid operation attempted: height {new_height}"
                + "cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = new_height

    def get_height(self) -> int:
        """Return the height of the plant"""

        return self.__height

    def get_growth(self) -> int:
        """Return the growth of the plant"""

        return self.__growth

    def grow(self) -> None:
        """Make a plant grow (+1 to height and growth)"""

        print(f"{self.name} grew 1cm")
        self.__height += 1
        self.__growth += 1

    def plant_type(self) -> str:
        """Return the type of plant"""

        return "plant"


class FloweringPlant(Plant):
    """FloweringPlant child of Plant. It has color and blooming parameters"""

    def __init__(self, name: str, height: int, color: str,
                 blooming: int) -> None:
        """Initialize the type FloweringPlant child of Plant"""

        super().__init__(name, height)
        self.blooming = blooming
        self.color = color

    def plant_type(self) -> str:
        """Return the type of the plant"""

        return "flowering"


class PrizeFlower(FloweringPlant):
    """PrizeFlower child of FloweringPlant. It has prize parameters"""

    def __init__(self, name: str, height: int, color: str, blooming: int,
                 prize: int) -> None:
        """Initialize a PrizeFlower

        Args:
            name (str): name of plant
            height (int): height of plant
            color (str): color of plant
            blooming (int): if it has bloomed or not (bool 1 or 0)
            prize (int): the prize of the plant
        """

        super().__init__(name, height, color, blooming)
        self.prize = prize

    def plant_type(self) -> str:
        """Get type of plant

        Returns:
            str: the type of the plant
        """

        return "prize"


class Garden:
    """class Garden. It has plants"""

    def __init__(self) -> None:
        """Initialize a Garden"""

        self.plants = []

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden

        Args:
            plant (Plant): A plant
        """

        self.plants.append(plant)

    @classmethod
    def create_garden(cls):
        """Create an instance of Garden

        Returns:
            Garden: a garden
        """
        return cls()

    def get_plants(self):
        """Return the plants of the garden

        Returns:
            Array: Array of plants
        """
        return self.plants


class GardenManager:
    """Make a manager of gardens"""

    def __init__(self, name: str) -> None:
        """Initialize a GardenManager

        Args:
            name (str): the name of the manager
        """
        self.name = name
        self.gardens = []

    class GardenStats:
        """Display information about a garden"""

        @staticmethod
        def show_garden(name: str, garden: Garden) -> None:
            """Display information of a given Garden

            Args:
                name (str): the name of the owner
                garden (Garden): the garden looking for
            """

            print(f"=== {name}'s Garden Report ===")
            print("Plants in garden:")
            i = 0
            growth = 0
            reg = 0
            flo = 0
            pri = 0
            for p in garden.plants:
                i += 1
                growth += p.get_growth()
                if p.plant_type() == "prize":
                    pri += 1
                elif p.plant_type() == "flowering":
                    flo += 1
                else:
                    reg += 1
                print(f"- {p.name}: {p.get_height()}cm", end="")
                if p.plant_type() == "flowering" or p.plant_type() == "prize":
                    print(f", {p.color} flowers", end="")
                    if p.blooming == 1:
                        print(" (blooming)", end="")
                    else:
                        print(" (bloomed)", end="")
                if type(p).__name__ == "prize":
                    print(f", Prize points : {p.prize}")
                print("")
            print(f"\nPlants added: {i}, Total growth: {growth}cm")
            print(
                f"Plant types: {reg} regular, {flo} flowering," f"{pri} prize flowers"
            )

    @classmethod
    def create_garden_network(cls):
        """Create a GardenManager

        Returns:
            GardenManager: An instance of a GardenManager
        """

        return cls("")

    def get_gardens(self) -> None:
        """_summary_

        Returns:
            Array: Array of gardens
        """

        return self.gardens

    def add_garden(self, garden: Garden) -> None:
        """Add a Garden to a GardenManager

        Args:
            garden (Garden): A Garden
        """

        self.gardens.append(garden)

    def add_plant_to_garden(self, garden: Garden, plant: Plant) -> None:
        """Add a Plant to a given Garden

        Args:
            garden (Garden): A Garden
            plant (Plant): A Plant
        """

        print(f"Added {plant.name} to {self.name}'s garden")
        self.gardens[garden].add_plant(plant)

    def grow(self, garden: Garden) -> None:
        """Make all Plant from a Garden grow()

        Args:
            garden (Garden): A Garden
        """

        print(f"{self.name} is helping all plants grow...")
        for p in self.gardens[garden].get_plants():
            p.grow()


if __name__ == "__main__":
    """Create a manager of a garden then make some changes in the garden"""

    print("=== Garden Management System Demo ===\n")
    alice = GardenManager.create_garden_network()
    alice.name = "Alice"
    bob = GardenManager("Bob")

    alice.add_garden(Garden.create_garden())
    alice.add_plant_to_garden(0, Plant("Oak Tree", 100))
    alice.add_plant_to_garden(0, FloweringPlant("Rose", 25, "red", 0))
    alice.add_plant_to_garden(0, PrizeFlower("Sunflower", 50, "yellow", 1, 10))
    print("")
    alice.grow(0)
    print("")
    GardenManager.GardenStats.show_garden(alice.name, alice.get_gardens()[0])
    print("")
