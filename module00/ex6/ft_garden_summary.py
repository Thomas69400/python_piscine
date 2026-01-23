def ft_garden_summary() -> None:
    """Prompt the user for garden information and print a short summary.

    Asks for a garden name and number of plants, then prints a formatted
    summary.
    """
    print("Enter garden name: ", end="")
    name: str = input()
    print("Enter number of plants: ", end="")
    nbr: str = input()
    print(f"Garden: {name}\nPlants: {nbr}\nStatus: Growing well!")
