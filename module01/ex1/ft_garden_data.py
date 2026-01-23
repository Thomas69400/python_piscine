class Plant:
    """Simple Plant data holder for registry."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize Plant with name, height (cm) and age (days)."""
        self.name: str = name
        self.height: int = height
        self.age: int = age


if __name__ == "__main__":
    """Print information about plants"""
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Tulip", 20, 25),
        Plant("Jonquil", 22, 20),
    ]
    print("=== Garden Plant Registry ===\n")
    for p in plants:
        print(p.name, ": ", p.height, "cm, ", p.age, " days old", sep="")
    print("\n=== End of Program ===")
