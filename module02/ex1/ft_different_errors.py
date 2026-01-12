def garden_operations(ope: str) -> int:
    """Try to make operations then catch the errors"""

    if ope == "NoError":
        return 5
    if ope == "ValueError":
        try:
            int("abc")
        except ValueError as e:
            print(f"Caught ValueError: {e}\n")
    if ope == "ZeroDivisionError":
        try:
            return 5 / 0
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}\n")
    if ope == "FileNotFoundError":
        try:
            open("missing.txt", 'r')
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}\n")
    if ope == "KeyError":
        try:
            my_dict = {"plant": "tomato"}
            my_dict["missing_plant"]
        except KeyError as e:
            print(f"Caught KeyError: {e}\n")


def test_error_types() -> None:
    """Test the function garden_operations()"""

    print("Testing ValueError...")
    garden_operations("ValueError")

    print("Testing ZeroDivisionError...")
    garden_operations("ZeroDivisionError")

    print("Testing FileNotFoundError...")
    garden_operations("FileNotFoundError")

    print("Testing KeyError...")
    garden_operations("KeyError")

    print("Testing multiple errors together...")
    garden_operations("NoError")
    garden_operations("ValueError")
    garden_operations("NoError")
    print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
