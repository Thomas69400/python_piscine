""" Exercise 3: Plant Factory
Create multiple Plant instances quickly with different starting values,
and display them in an organized format.
"""

from typing import List, Tuple


class Plant:
    """Represent a plant with a name, height (cm), and age (days).

    Methods:
        get_info: Return a formatted string describing the plant.
    """

    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        """Initialize a Plant with starting information."""
        self.name: str = name
        self.height_cm: int = height_cm
        self.age_days: int = age_days

    def get_info(self) -> str:
        """Return a formatted string describing the plant."""
        return f"{self.name} ({self.height_cm}cm, {self.age_days} days)"


class PlantFactory:
    """
    Create a list of Plant objects from a list of specs.

    Each spec is: (name, starting_height_cm, starting_age_days)
    """

    def create_plants(
        self,
        specs: List[Tuple[str, int, int]]
    ) -> List[Plant]:
        """Create Plant instances from specs and return the list of created
        Plant objects."""
        plants: List[Plant] = []
        for name, height_cm, age_days in specs:
            plants.append(Plant(name, height_cm, age_days))
        return plants

    @staticmethod
    def display_created_plants(plants: List[Plant]) -> None:
        """Display all created plants and the total count."""
        print("=== Plant Factory Output ===")
        count: int = 0
        for plant in plants:
            print(f"Created: {plant.get_info()}")
            count += 1
        print(f"Total plants created: {count}")


if __name__ == "__main__":
    plant_specs = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    factory = PlantFactory()
    plants = factory.create_plants(plant_specs)

    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.get_info()}")
    print()
    print(f"Total plants created: {len(plants)}")
