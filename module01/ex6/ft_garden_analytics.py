"""Classes modeling plants, gardens and managers with simple reporting
helpers."""
from typing import List, Dict


class Plant:
    """Represent a generic plant with a name, height (cm) and growth counter.

    Attributes:
        name (str): The plant's name.
        __height (int): Current height in cm.
        __growth (int): Cumulative growth in cm since creation.
    """

    def __init__(self, name: str, height: int) -> None:
        """Initialize a Plant.

        Args:
            name: Plant name.
            height: Initial height in cm.
        """
        self.name: str = name
        self.__height: int = height
        self.__growth: int = 0

    def set_height(self, new_height: int) -> None:
        """Set the plant height if non-negative.

        Args:
            new_height: New height in cm. Negative values are rejected.
        """

        if new_height < 0:
            print(
                f"Invalid operation attempted: height {new_height}"
                + "cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = new_height

    def get_height(self) -> int:
        """Return the plant height in cm."""

        return self.__height

    def get_growth(self) -> int:
        """Return cumulative growth in cm."""

        return self.__growth

    def grow(self) -> None:
        """Increase height and growth by 1 cm and print a short message."""

        print(f"{self.name} grew 1cm")
        self.__height += 1
        self.__growth += 1

    def plant_type(self) -> str:
        """Return the type label for the plant."""

        return "plant"

    def validate_height(self) -> bool:
        """Return True if height is non-negative."""

        if self.get_height() < 0:
            return False
        return True

    def get_info(self) -> str:
        """Return a short printable description of the plant."""

        return f"- {self.name}: {self.get_height()}cm"


class FloweringPlant(Plant):
    """A Plant that has flower color and blooming state."""

    def __init__(self, name: str, height: int, color: str,
                 blooming: str) -> None:
        """Initialize a FloweringPlant.

        Args:
            name: Plant name.
            height: Initial height in cm.
            color: Flower color.
            blooming: Blooming state description.
        """

        super().__init__(name, height)
        self.blooming = blooming
        self.color = color

    def plant_type(self) -> str:
        """Return 'flowering' as the type label."""

        return "flowering"

    def get_info(self) -> str:
        """Return detailed info including color and blooming."""

        return f"- {self.name}: {self.get_height()}cm, " + \
            f"{self.color} flowers ({self.blooming})"


class PrizeFlower(FloweringPlant):
    """A FloweringPlant that carries a prize point value."""

    def __init__(self, name: str, height: int, color: str, blooming: str,
                 prize: int) -> None:
        """Initialize a PrizeFlower.

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
        """Return 'prize' as the type label."""

        return "prize"

    def get_info(self) -> str:
        """Return detailed info including prize points."""

        return f"- {self.name}: {self.get_height()}cm, " + \
            f"{self.color} flowers ({self.blooming}), " + \
            f"Prize points: {self.prize}"


class Garden:
    """Container for Plant objects."""

    def __init__(self) -> None:
        """Create an empty garden."""

        self.plants: List[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        """Add a Plant instance to the garden."""

        self.plants.append(plant)

    @classmethod
    def create_garden(cls) -> "Garden":
        """Return a new Garden instance."""

        return cls()

    def get_plants(self) -> List[Plant]:
        """Return the list of plants in the garden."""

        return self.plants


class GardenManager:
    """Manage multiple gardens and report statistics.

    Attributes:
        name (str): Manager name.
        gardens (List[Garden]): Gardens managed by this manager.
        total_garden (int): Class-level counter of total gardens added.
    """
    total_garden: int = 0

    def __init__(self, name: str) -> None:
        """Initialize a GardenManager with a name."""

        self.name: str = name
        self.gardens: List[Garden] = []

    class GardenStats:
        """Collection of static helpers to display garden statistics."""

        @staticmethod
        def show_types(garden: Garden) -> str:
            """Return a summary string of plant types counts in the garden."""

            reg: int = 0
            flo: int = 0
            pri: int = 0
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
            """Return a summary string containing number of plants and total
            growth."""

            growth: int = 0
            for p in garden.get_plants():
                growth += p.get_growth()
            return f"\nPlants added: {len(garden.get_plants())}, " + \
                f"Total growth: {growth}cm"

        @staticmethod
        def get_garden_score(garden_managers: List["GardenManager"]) -> str:
            """Compute prize-based scores for each manager.

            Args:
                garden_managers: List of GardenManager instances to score.

            Returns:
                A formatted string listing each manager and their score.
            """

            scores: Dict[str, int] = {}
            for manager in garden_managers:
                scores.update({manager.name: 0})
            for manager in garden_managers:
                for garden in manager.get_gardens():
                    for plant in garden.get_plants():
                        if isinstance(plant, PrizeFlower):
                            scores[manager.name] += plant.prize
            msg: str = "Garden scores - "
            for score in scores:
                msg += f"{score}: {scores[score]}, "
            return msg.rstrip(", ")

        @classmethod
        def show_garden(cls, name: str,
                        garden: Garden,
                        garden_managers: List["GardenManager"]) -> None:
            """Print a full garden report for a manager."""

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
    def create_garden_network(cls) -> "GardenManager":
        """Create and return a GardenManager placeholder for building a
        network."""

        return cls("")

    def get_gardens(self) -> List[Garden]:
        """Return gardens managed by this manager."""

        return self.gardens

    def add_garden(self, garden: Garden) -> None:
        """Add a Garden to this manager and increment global counter."""

        GardenManager.total_garden += 1
        self.gardens.append(garden)

    def add_plant_to_garden(self, garden_index: int, plant: Plant) -> None:
        """Add a Plant to a garden referenced by index."""

        print(f"Added {plant.name} to {self.name}'s garden")
        self.gardens[garden_index].add_plant(plant)

    def grow(self, garden_index: int) -> None:
        """Invoke grow() on every plant in the specified garden."""

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
