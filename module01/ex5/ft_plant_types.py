class Plant:
    """Basic plant with name, height (cm) and age (days)."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize Plant attributes."""

        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> None:
        """Print information about the plant"""

        print(
            f"{self.name} ({type(self).__name__}): "
            f"{self.height}cm,"
            f" {self.age} days",
            end="",
        )


class Flower(Plant):
    """A Plant that has a color and can bloom once."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize Flower with color and bloom state"""

        super().__init__(name, height, age)
        self.color: str = color
        self.bloomed: int = 0

    def bloom(self) -> None:
        """Trigger bloom if not already bloomed"""

        if self.bloomed == 0:
            print(f"{self.name} is blooming beautifully!")
            self.bloomed = 1
        else:
            print(f"{self.name} has already bloomed!")


class Tree(Plant):
    """A Plant that has a trunk diameter and can compute shade area."""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initialize Tree with trunk diameter in cm."""

        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        """Print the approximate shade area produced by the tree"""

        shade = self.height // self.trunk_diameter
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    """A Plant with harvest season and nutritional value metadata."""

    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        """Initialize Vegetable with harvest season and nutrition info"""

        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value


if __name__ == "__main__":
    """Create a multiple types of plants and show their informations"""

    plants = [Flower("Rose", 25, 30, "red"), Flower("Tulip", 20, 15, "yellow")]
    trees = [Tree("Oak", 500, 1825, 50), Tree("Ficus", 400, 452, 20)]
    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 20, 56, "winter", "vitamin D"),
    ]
    print("=== Garden Plant Types ===\n")
    for p in plants:
        p.get_info()
        print(f", {p.color} color")
        p.bloom()
    print("")
    for t in trees:
        t.get_info()
        print(f", {t.trunk_diameter}cm diameter")
        t.produce_shade()
    print("")
    for v in vegetables:
        v.get_info()
        print(f", {v.harvest_season} harvest")
        print(f"{v.name} is rich in {v.nutritional_value}")
