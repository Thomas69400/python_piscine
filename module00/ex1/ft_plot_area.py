def ft_plot_area() -> None:
    """Prompt the user for plot dimensions and print the area."""
    print("Enter length: ", end="")
    length: int = int(input())
    print("Enter width: ", end="")
    width: int = int(input())
    area: int = length * width
    print(f"Plot area: {area}")
