def ft_plant_age() -> None:
    """Ask the user for the plant's age in days and report readiness for
    harvest."""

    print("Enter plant age in days: ", end="")
    age: int = int(input())
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
