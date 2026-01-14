def ft_garden_summary():
    """Print a summary of a garden"""

    print("Enter garden name: ", end="")
    name = input()
    print("Enter number of plants: ", end="")
    nbr = input()
    print(f"Garden: {name}\nPlants: {nbr}\nStatus: Growing well!")
