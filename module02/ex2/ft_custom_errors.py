class GardenError(Exception):
    """Define custom error for Garden"""

    def __init__(self, message: str) -> None:
        """Initialize the error message"""

        self.message = message


class PlantError(GardenError):
    """Define custom error for Plant"""

    def __init__(self, message: str) -> None:
        """Initialize the error message"""

        super().__init__(message)


class WaterError(GardenError):
    """Define custom error for Water"""

    def __init__(self, message: str) -> None:
        """Initialize the error message"""

        super().__init__(message)


def garden_operations(ope: str) -> None:
    """Try to make operations then catch the errors"""

    if ope == "PlantError":
        raise PlantError("Caught PlantError: The tomato plant is wilting!")
    if ope == "WaterError":
        raise WaterError(
            "Caught a garden error: Not enough water in the tank!")


def test_error_types() -> None:
    """Test the function garden_operations()"""

    try:
        print("Testing PlantError...")
        garden_operations("PlantError")
    except PlantError as e:
        print(e)
    try:
        print("\nTesting WaterError...")
        garden_operations("WaterError")
    except WaterError as e:
        print(e)
    print("\nTesting catching all garden errors...")
    try:
        garden_operations("PlantError")
    except GardenError as e:
        print(e)
    try:
        garden_operations("WaterError")
    except GardenError as e:
        print(e)

    print("\nAll custom error types work correctly!")


print("=== Custom Garden Errors Demo ===\n")
test_error_types()
