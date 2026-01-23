"""Simple demo printing a single plant summary."""

if __name__ == "__main__":
    """Print information about a plant"""

    plant: str = "Rose"
    height: int = 25
    age: int = 30
    print("=== Welcome to My Garden ===\n")
    print("Plant:", plant)
    print("Height: ", height, "cm", sep="")
    print("Age:", age, "days")
    print("\n=== End of Program ===")
