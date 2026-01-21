def garden_operations() -> int:
    """Try to make operations then catch the errors"""

    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    try:
        print("Testing ZeroDivisionError...")
        return 5 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    try:
        print("Testing FileNotFoundError...")
        open("missing.txt", 'r')
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    try:
        print("Testing KeyError...")
        my_dict = {"plant": "tomato"}
        my_dict["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    try:
        print("Testing multiple errors together...")
        open("missing.txt", 'r')
    except (KeyError, FileNotFoundError, ZeroDivisionError, ValueError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    """Test the function garden_operations()"""

    garden_operations()

    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
