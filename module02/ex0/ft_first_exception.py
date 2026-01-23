from typing import Optional


def check_temperature(temp_str: str) -> Optional[int]:
    """Convert a temperature string to int and validate range for plants.

    Returns:
        Optional[int]: the integer temperature if valid, otherwise None
    """

    try:
        temp_int: int = int(temp_str)
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None
    if (temp_int > 40):
        print(f"Error: {temp_int}°C is too hot for plants (max 40°C)\n")
        return None
    elif (temp_int < 0):
        print(f"Error: {temp_int}°C is too cold for plants (min 0°C)\n")
        return None
    print(f"Temperature {temp_int}°C is perfect for plants!\n")
    return temp_int


def test_temperature_input(temp_str: str) -> None:
    """Test if a temperature string is valid for plants

    Args:
        temp_str (str): The temperature to test
    """

    print(f"Testing temperature: {temp_str}")
    check_temperature(temp_str)


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input("25")
    test_temperature_input("abc")
    test_temperature_input("100")
    test_temperature_input("-50")
    print("All tests completed - program didn't crash!")
