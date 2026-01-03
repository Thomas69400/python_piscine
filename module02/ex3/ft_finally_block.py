def water_plants(plant_list):
    """Print all the plant getting water

    Args:
        plant_list (array): an array containing plant

    Raises:
        Exception: error message when bad name
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


def test_watering_system():
    """Test all errors for water_plants()

    Args:
        plant_list (array): an array containing plant
    """

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
