#!/usr/bin/env python3

class Plant:
    """Define all information about a plant"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a plant and define her attributes"""

        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, new_height: int) -> None:
        """Set the height of the plant can't be negative"""

        if (new_height < 0):
            print(f"Invalid operation attempted: height {new_height}"
                  "cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = new_height
        print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, new_age: int) -> None:
        """Set the age of the plant can't be negative"""

        if (new_age < 0):
            print(f"Invalid operation attempted: age {new_age}"
                  " days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__age = new_age
        print(f"Age updated: {self.__age} days [OK]")

    def get_height(self) -> int:
        """Return the height of the plant"""

        return self.__height

    def get_age(self) -> int:
        """Return the age of the plant"""

        return self.__age

    def get_info(self) -> None:
        """Display informations about the plant"""
        print(f"Current plant: {self.name} ({self.__height}cm,"
              f" {self.__age} days)")


if __name__ == "__main__":
    """Create a plant and try to modify its height and age"""

    plant = Plant("Rose", 25, 30)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.name}")
    plant.set_height(80)
    plant.set_age(2)
    print("")
    plant.set_height(-5)
    plant.set_age(-100)
    print("")
    plant.get_info()
