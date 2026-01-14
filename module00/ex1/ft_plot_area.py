def ft_plot_area():
    """Ask user a height and a length"""

    print("Enter length: ", end="")
    len = int(input())
    print("Enter width: ", end="")
    wid = int(input())
    print(f"Plot area: {len * wid}")
