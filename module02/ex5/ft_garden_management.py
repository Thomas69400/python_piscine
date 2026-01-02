class Plant:
    """A Plant. It has a name, a water level and sunlight"""

    def __init__(self, name: str, water: int, sunlight: int) -> None:
        """Initialize a Plant

        Args:
            name (str): the name of the Plant
            water (int): the water level of the Plant
            sunlight (int): the sunlight of the Plant
        """

        self.name = name
        self.water = water
        self.sunlight = sunlight

    def add_water(self, watering: int) -> None:
        """Add water to a plant

        Args:
            watering (int): the water to add to the plant
        """

        self.water += watering

    def get_info(self):
        """Print information about a Plant"""

        print(f"{self.name}: healthy (water: {self.water}," +
              f" sun: {self.sunlight})")


class Garden:
    """A Garden. It contains plants"""

    def __init__(self, tank: int) -> None:
        """Initialize a Garden. It has no plants

        Args:
            tank (int): the water the garden have to give water to plants
        """

        self.plants = []
        self.tank = tank

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden

        Args:
            plant (Plant): a plant to add to the garden
        """

        self.plants.append(plant)


class GardenError(Exception):
    """Handle error of Garden class"""

    def __init__(self, msg: str) -> None:
        """Initialize a GardenError

        Args:
            msg (str): the message to display
        """

        super().__init__(msg)


class GardenManager:
    """Class to manager a Garden"""

    def __init__(self):
        """Initialize a Garden"""

        self.garden = Garden(0)

    @staticmethod
    def check_plant_health(plant_name: str, water_level: int,
                           sunlight_hours: int) -> int:
        """If error occurs on a variable then raise an error

        Args:
            plant_name (str): the name of a plant
            water_level (int): the water level of plant
            sunlight_hours (int): the sunlight of plant

        Raises:
            ValueError: error message when bad name
            ValueError: error message when water_level > 10
            ValueError: error message when sunlight_hours < 2

        Returns:
            str: success message
        """

        if plant_name is None or plant_name == "":
            raise ValueError("Plant name cannot be empty!")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)")
        return 1

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden, throw error if plant has no name or
        water_level > 10 or sunlight_hours < 2

        Args:
            plant (Plant): a plant to add to the garden
        """

        try:
            self.check_plant_health(plant.name, plant.water, plant.sunlight)
            self.garden.add_plant(plant)
            print(f"Added {plant.name} successfully")
        except ValueError as e:
            print(f"Error: {e}")

    def water_plants(self):
        """Watering all the plant"""

        print("Opening watering system")
        for p in self.garden.plants:
            if p is None:
                raise Exception(f"Cannot give water to {p}")
            if self.garden.tank < 5:
                raise GardenError("Not enough water in tank")
            p.add_water(5)
            self.garden.tank -= 5
            print(f"Watering {p.name} - success")

    def get_plants(self):
        """Return the plants of the garden

        Returns:
            array: all plants of garden
        """

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
    finally:
        print("Closing watering system (cleanup)")

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
