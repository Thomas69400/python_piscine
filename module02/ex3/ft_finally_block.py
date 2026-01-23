from typing import List, Optional


def water_plants(plant_list: List[Optional[str]]) -> None:
    """Open the watering system and water each plant; always perform cleanup.

    Args:
        plant_list (List[Optional[str]]): a list of plant names, items may
        be None
    Raises:
        Exception: raised when a plant name is invalid (None or empty)
    """

    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise Exception("None")
            print(f"Watering {plant}")
        print("Watering completed successfully!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Run example scenarios demonstrating the watering system behavior."""

    print("\nTesting normal watering...")
    try:
        plants = ["tomato", "lettuce", "carrots"]
        water_plants(plants)
    except Exception as e:
        print(f"Error: Cannot water {e} - invalid plant!")

    print("\nTesting with error...")
    try:
        plants = ["tomato", None, "carrots"]
        water_plants(plants)
    except Exception as e:
        print(f"Error: Cannot water {e} - invalid plant!")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
