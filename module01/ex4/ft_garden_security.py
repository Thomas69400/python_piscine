class SecurePlant:
    """A plant model with private height and age attributes and safe
    setters."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize SecurePlant.

        Args:
            name: Plant name.
            height: Initial height in cm.
            age: Initial age in days.
        """
        self.name: str = name
        self.__height: int = height
        self.__age: int = age

    def set_height(self, new_height: int) -> None:
        """Safely set the plant height if non-negative"""

        if (new_height < 0):
            print(f"Invalid operation attempted: height {new_height}"
                  "cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = new_height
        print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, new_age: int) -> None:
        """Safely set the plant age if non-negative"""

        if (new_age < 0):
            print(f"Invalid operation attempted: age {new_age}"
                  " days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__age = new_age
        print(f"Age updated: {self.__age} days [OK]")

    def get_height(self) -> int:
        """Return the plant height in cm"""

        return self.__height

    def get_age(self) -> int:
        """Return the plant age in days"""

        return self.__age

    def get_info(self) -> None:
        """Print a summary of the plant's current state"""
        print(f"Current plant: {self.name} ({self.__height}cm,"
              f" {self.__age} days)")


if __name__ == "__main__":
    """Create a plant and try to modify its height and age"""

    plant = SecurePlant("Rose", 25, 30)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.name}")
    plant.set_height(80)
    plant.set_age(2)
    print("")
    plant.set_height(-5)
    plant.set_age(-100)
    print("")
    plant.get_info()
