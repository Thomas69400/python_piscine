from typing import List


class Plant:
    """A Plant with a name, water level and sunlight.

    Attributes:
        name (str): Plant name.
        water (int): Water level (1-10).
        sunlight (int): Sunlight hours (2-12).
    """

    name: str
    water: int
    sunlight: int

    def __init__(self, name: str, water: int, sunlight: int) -> None:
        """Initialize a Plant.

        Args:
            name (str): the name of the Plant
            water (int): the water level of the Plant
            sunlight (int): the sunlight of the Plant
        """
        self.name = name
        self.water = water
        self.sunlight = sunlight

    def add_water(self, watering: int) -> None:
        """Add water to a plant.

        Args:
            watering (int): amount of water to add
        """
        self.water += watering

    def get_info(self) -> None:
        """Print information about the plant."""
        print(f"{self.name}: healthy (water: {self.water}," +
              f" sun: {self.sunlight})")


class Garden:
    """A Garden that contains plants and a water tank."""

    plants: List[Plant]
    tank: int

    def __init__(self, tank: int) -> None:
        """Initialize a Garden.

        Args:
            tank (int): the water available in the garden's tank
        """
        self.plants = []
        self.tank = tank

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        self.plants.append(plant)


class GardenError(Exception):
    """Custom error type for Garden-related errors."""

    def __init__(self, msg: str) -> None:
        """Initialize a GardenError with a message."""
        super().__init__(msg)


class GardenManager:
    """Manager for Garden operations."""

    garden: Garden

    def __init__(self) -> None:
        """Initialize a GardenManager with an empty Garden."""
        self.garden = Garden(0)

    @staticmethod
    def check_plant_health(plant_name: str, water_level: int,
                           sunlight_hours: int) -> int:
        """Validate plant parameters, raise ValueError on invalid input.

        Returns:
            int: 1 on success (validation passed)
        """
        if plant_name is None or plant_name == "":
            raise ValueError("Plant name cannot be empty!")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        if sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too high " +
                             "(max 12)")
        return 1

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden after validation."""
        try:
            self.check_plant_health(plant.name, plant.water, plant.sunlight)
            self.garden.add_plant(plant)
            print(f"Added {plant.name} successfully")
        except ValueError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        """Water all plants using the garden tank, ensure cleanup."""
        print("Opening watering system")
        try:
            for p in self.garden.plants:
                if p is None or p == "":
                    raise Exception("None")
                if self.garden.tank < 5:
                    raise GardenError("Not enough water in tank")
                p.add_water(5)
                self.garden.tank -= 5
                print(f"Watering {p.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def get_plants(self) -> List[Plant]:
        """Return the list of plants in the garden."""
        return self.garden.plants


if __name__ == "__main__":
    print("=== Garden Management System ===\n")

    manager = GardenManager()
    print("Adding plants to garden...")
    manager.add_plant(Plant("tomato", 5, 3))
    manager.add_plant(Plant("lettuce", 10, 3))
    manager.add_plant(Plant("", 5, 3))

    print("\nWatering plants...")
    manager.garden.tank = 14
    try:
        manager.water_plants()
    except Exception as e:
        print(f"Error: {e}")

    print("\nChecking plant health...")
    for p in manager.get_plants():
        try:
            GardenManager.check_plant_health(p.name, p.water, p.sunlight)
            p.get_info()
        except Exception as e:
            print(f"Error checking {p.name}: {e}")

    print("\nTesting error recovery...")
    try:
        manager.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")
