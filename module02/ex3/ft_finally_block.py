def water_plants(plant_list):
    """Print all the plant getting water

    Args:
        plant_list (array): an array containing plant
    """

    print("Opening watering system")
    for p in plant_list:
        if p is None:
            raise Exception(p)
        print(f"Watering {p}")


def test_watering_system(plant_list):
    """Test all errors for water_plants()

    Args:
        plant_list (array): an array containing plant
    """

    try:
        water_plants(plant_list)
    except Exception as e:
        print(f"Error: Cannot water {e} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    test_watering_system(plants)
    print("\nTesting with error...")
    plants[1] = None
    test_watering_system(plants)
    print("")
    print("Cleanup always happens, even with errors!")
