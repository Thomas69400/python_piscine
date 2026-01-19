class Plant:
    """Define all information about a plant"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a plant and define its attributes"""

        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        """Display informations about the plant"""

        print(
            f"{self.name} ({type(self).__name__}): "
            f"{self.height}cm,"
            f" {self.age} days",
            end="",
        )


class Flower(Plant):
    """Flower child of class Plant, get a color and can bloom"""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Create a flower and define her attributes with color"""

        super().__init__(name, height, age)
        self.color = color
        self.bloomed = 0

    def bloom(self) -> None:
        """If not bloom then bloom"""

        if self.bloomed == 0:
            print(f"{self.name} is blooming beautifully!")
            self.bloomed = 1
        else:
            print(f"{self.name} has already bloomed!")


class Tree(Plant):
    """Tree child of class Plant, get a trunk_diameter and can make shade"""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Create a tree and define his attributes with trunk_diameter"""

        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Display information about the size of shade created by the tree"""

        shade = self.height // self.trunk_diameter
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    """Vegetable child of class Plant, get a harvest season and a nutritional
        value"""

    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        """Create a plant and define her attributes"""

        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


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
