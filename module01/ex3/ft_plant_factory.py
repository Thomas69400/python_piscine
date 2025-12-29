#!/usr/bin/env python3


class Plant:
    """Define all information about a plant"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a plant and define her attributes"""
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    """Create 5 plants and display their informations"""

    plants = [
        Plant("Rose", 25, 30),
        Plant("Tulip", 20, 25),
        Plant("Jonquil", 22, 20),
        Plant("Cactus", 5, 90),
        Plant("Hibiscus", 90, 453),
    ]
    print("=== Plant Factory Output ===")
    n_plant = 0
    for p in plants:
        print(f"Created: {p.name} ({p.height}cm, {p.age} days)")
        n_plant += 1
    print(f"\nTotal plants created: {n_plant}")
