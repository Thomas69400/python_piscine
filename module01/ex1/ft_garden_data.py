class Plant:
    """Define all information about a plant"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Create a plant and define its attributes attributes"""
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    """Print information about plants"""

    plants = [
        Plant("Rose", 25, 30),
        Plant("Tulip", 20, 25),
        Plant("Jonquil", 22, 20),
    ]
    print("=== Garden Plant Registry ===\n")
    for p in plants:
        print(p.name, ": ", p.height, "cm, ", p.age, " days old", sep="")
    print("\n=== End of Program ===")
