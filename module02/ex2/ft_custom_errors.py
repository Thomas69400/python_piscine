class GardenError(Exception):
    """Define custom error for Garden"""

    def __init__(self, message: str) -> None:
        """Initialize the error message"""

        self.message = message
        super().__init__(self.message)


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
        raise PlantError("The tomato plant is wilting!")
    if ope == "WaterError":
        raise WaterError(
            "Not enough water in the tank!")


def test_error_types() -> None:
    """Test the function garden_operations()"""

    try:
        print("Testing PlantError...")
        garden_operations("PlantError")
    except PlantError as e:
        print(f"Caught a garden error: {e}")

    try:
        print("\nTesting WaterError...")
        garden_operations("WaterError")
    except WaterError as e:
        print(f"Caught a garden error: {e}")
        
    print("\nTesting catching all garden errors...")
    try:
        garden_operations("PlantError")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        garden_operations("WaterError")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_error_types()
