"""Custom exception types for garden domain and a small demonstration."""


class GardenError(Exception):
    """Custom exception base class for garden domain errors."""

    message: str

    def __init__(self, message: str) -> None:
        """Initialize the error message."""

        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    """Exception for plant-related errors."""

    def __init__(self, message: str) -> None:
        """Initialize a PlantError with a message."""

        super().__init__(message)


class WaterError(GardenError):
    """Exception for water-related errors."""

    def __init__(self, message: str) -> None:
        """Initialize a WaterError with a message."""

        super().__init__(message)


def garden_operations(ope: str) -> None:
    """Perform a garden operation that may raise a custom error.

    Args:
        ope (str): operation name that triggers a specific error
    """

    if ope == "PlantError":
        raise PlantError("The tomato plant is wilting!")
    if ope == "WaterError":
        raise WaterError(
            "Not enough water in the tank!")


def test_error_types() -> None:
    """Demonstrate raising and catching custom garden errors"""

    try:
        print("Testing PlantError...")
        garden_operations("PlantError")
    except PlantError as e:
        print(f"Caught a PlantError: {e}")

    try:
        print("\nTesting WaterError...")
        garden_operations("WaterError")
    except WaterError as e:
        print(f"Caught a WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        garden_operations("PlantError")
    except GardenError as e:
        print(f"Caught a GardenError: {e}")
    try:
        garden_operations("WaterError")
    except GardenError as e:
        print(f"Caught a GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    test_error_types()
