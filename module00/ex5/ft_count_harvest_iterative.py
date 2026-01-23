def ft_count_harvest_iterative() -> None:
    """Iteratively prompt for days until harvest and print each day."""
    print("Days until harvest: ", end="")
    days: int = int(input())
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")
