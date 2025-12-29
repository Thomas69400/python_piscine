#!/usr/bin/env python3


class Plant:
    """Define all information about a plant"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a plant and define her attributes"""

        self.name = name
        self.height = height
        self.age = age
        self.growth = 0

    def grow(self) -> None:
        """Augment the height of the plant by 7 & set the growth param to 7"""

        self.height += 7
        self.growth = 7

    def get_older(self) -> None:
        """Augment the age of the plant by 7"""

        self.age += 7

    def get_info(self) -> None:
        """Display informations about the plant"""

        print(f"{p.name} : {p.height} cm, {p.age} days old")


if __name__ == "__main__":
    """Create a plant then make it grow and age"""

    plants = {Plant("Rose", 25, 30)}
    print("=== Day 1 ===")
    for p in plants:
        p.get_info()
        p.grow()
        p.get_older()
    print("=== Day 7 ===")
    for p in plants:
        p.get_info()
        print(f"Growth this week: +{p.growth}cm")
