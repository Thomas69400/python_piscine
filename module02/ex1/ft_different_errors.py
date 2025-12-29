def garden_operations(ope: str) -> int:
    """Try to make operations then catch the errors"""

    if ope == "NoError":
        return 5
    if ope == "ValueError":
        return int(ope)
    if ope == "ZeroDivisionError":
        return 5 / 0
    if ope == "FileNotFoundError":
        return open("missing.txt", 'r')
    if ope == "KeyError":
        return ope[0]


def test_error_types() -> None:
    """Test the function garden_operations()"""

    try:
        print("Testing ValueError...")
        garden_operations("ValueError")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        print("Testing FileNotFoundError...")
        garden_operations("FileNotFoundError")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    try:
        print("Testing KeyError...")
        garden_operations("KeyError")
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
    try:
        print("Testing multiple errors together...")
        garden_operations("NoError")
        garden_operations("ValueError")
        garden_operations("NoError")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


print("=== Garden Error Types Demo ===\n")
test_error_types()
