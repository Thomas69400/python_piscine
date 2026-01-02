def garden_operations(ope: str) -> int:
    """Try to make operations then catch the errors"""

    if ope == "NoError":
        return 5
    if ope == "ValueError":
        return int("abc")
    if ope == "ZeroDivisionError":
        return 5 / 0
    if ope == "FileNotFoundError":
        return open("missing.txt", 'r')
    if ope == "KeyError":
        my_dict = {"plant": "tomato"}
        return my_dict["missing_plant"]


def test_error_types() -> None:
    """Test the function garden_operations()"""

    try:
        print("Testing ValueError...")
        garden_operations("ValueError")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    try:
        print("Testing ZeroDivisionError...")
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    try:
        print("Testing FileNotFoundError...")
        garden_operations("FileNotFoundError")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    try:
        print("Testing KeyError...")
        garden_operations("KeyError")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    try:
        print("Testing multiple errors together...")
        garden_operations("NoError")
        garden_operations("ValueError")
        garden_operations("NoError")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
