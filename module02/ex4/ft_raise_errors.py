def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """If error occurs on a variable then raise an error

    Args:
        plant_name (str): the name of a plant
        water_level (int): the water level of plant
        sunlight_hours (int): the sunlight of plant

    Raises:
        ValueError: error message when bad name
        ValueError: error message when water_level > 10
        ValueError: error message when water_level < 1
        ValueError: error message when sunlight_hours < 2
        ValueError: error message when sunlight_hours > 12

    Returns:
        str: success message
    """

    if plant_name is None or plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high" +
                         "(max 12)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """Test all errors types of check_plant_health()"""

    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 10, 10))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        print(check_plant_health("", 10, 10))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        print(check_plant_health("tomato", 15, 10))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 10, 0))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
