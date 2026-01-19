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

    def validate_height(self) -> bool:
        if self.get_height() < 0:
            return False
        return True

    def get_info(self) -> str:
        return f"- {self.name}: {self.get_height()}cm"


class FloweringPlant(Plant):
    """FloweringPlant child of Plant. It has color and blooming parameters"""

    def __init__(self, name: str, height: int, color: str,
                 blooming: str) -> None:
        """Initialize a FloweringPlant

        Args:
            name (str): name of plant
            height (int): height of plant
            color (str): color of plant
            blooming (str): if flower has bloom
        """

        super().__init__(name, height)
        self.blooming = blooming
        self.color = color

    def plant_type(self) -> str:
        """Return the type of the plant"""

        return "flowering"

    def get_info(self) -> str:
        return f"- {self.name}: {self.get_height()}cm, " + \
            f"{self.color} flowers ({self.blooming})"


class PrizeFlower(FloweringPlant):
    """PrizeFlower child of FloweringPlant. It has prize parameters"""

    def __init__(self, name: str, height: int, color: str, blooming: str,
                 prize: int) -> None:
        """Initialize a PrizeFlower

        Args:
            name (str): name of plant
            height (int): height of plant
            color (str): color of plant
            blooming (str): if flower has bloom
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

    def get_info(self) -> str:
        return f"- {self.name}: {self.get_height()}cm, " + \
            f"{self.color} flowers ({self.blooming}), " + \
            f"Prize points: {self.prize}"


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
    total_garden = 0

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
        def show_types(garden: Garden) -> str:
            reg = 0
            flo = 0
            pri = 0
            for p in garden.get_plants():
                if p.plant_type() == "prize":
                    pri += 1
                elif p.plant_type() == "flowering":
                    flo += 1
                else:
                    reg += 1
            return f"Plant types: {reg} regular, {flo} flowering, " + \
                f"{pri} prize flowers"

        @staticmethod
        def show_stats(garden: Garden) -> str:
            growth = 0
            for p in garden.get_plants():
                growth += p.get_growth()
            return f"\nPlants added: {len(garden.get_plants())}, " + \
                f"Total growth: {growth}cm"

        @staticmethod
        def get_garden_score(garden_managers) -> str:
            scores = {}
            for manager in garden_managers:
                scores.update({manager.name: 0})
            for manager in garden_managers:
                for garden in manager.get_gardens():
                    for plant in garden.get_plants():
                        if isinstance(plant, PrizeFlower):
                            scores[manager.name] += plant.prize
            msg = "Garden scores - "
            for score in scores:
                msg += f"{score}: {scores[score]}, "
            return msg.rstrip(", ")

        @classmethod
        def show_garden(cls, name: str,
                        garden: Garden, garden_managers) -> None:
            print(f"=== {name}'s Garden Report ===")
            print("Plants in garden:")

            valid: bool = True
            for p in garden.get_plants():
                valid = p.validate_height()
                print(p.get_info())
            print(cls.show_stats(garden))
            print(cls.show_types(garden))
            print(f"\nHeight validation test: {valid}")
            print(cls.get_garden_score(garden_managers))
            print(f"Total gardens managed: {GardenManager.total_garden}")

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
        GardenManager.total_garden += 1
        self.gardens.append(garden)

    def add_plant_to_garden(self, garden_index: int, plant: Plant) -> None:
        """Add a Plant to a given Garden

        Args:
            garden_index (int): the index of the garden
            plant (Plant): A Plant
        """

        print(f"Added {plant.name} to {self.name}'s garden")
        self.gardens[garden_index].add_plant(plant)

    def grow(self, garden_index: int) -> None:
        """Make all Plant from a Garden grow()

        Args:
            garden_index (int): the index of the garden
        """

        print(f"{self.name} is helping all plants grow...")
        for p in self.gardens[garden_index].get_plants():
            p.grow()


if __name__ == "__main__":
    """Create a manager of a garden then make some changes in the garden"""

    print("=== Garden Management System Demo ===\n")
    alice: GardenManager = GardenManager.create_garden_network()
    alice.name = "Alice"
    bob: GardenManager = GardenManager("Bob")

    alice.add_garden(Garden.create_garden())
    alice.add_plant_to_garden(0, Plant("Oak Tree",
                                       100))
    alice.add_plant_to_garden(0, FloweringPlant("Rose",
                                                25,
                                                "red",
                                                "blooming"))
    alice.add_plant_to_garden(0, PrizeFlower("Sunflower",
                                             50,
                                             "yellow",
                                             "blooming",
                                             10))
    print("")
    alice.grow(0)
    print("")
    bob.add_garden(Garden())
    bob.gardens[0].plants.append(Plant("Oak Tree", 100))
    garden_managers = [alice, bob]
    GardenManager.GardenStats.show_garden(
        alice.name, alice.get_gardens()[0], garden_managers)
    print("")
