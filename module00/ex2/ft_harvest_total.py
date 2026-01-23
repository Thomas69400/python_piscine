def ft_harvest_total() -> None:
    """Prompt harvest amounts for three days and print the total harvest."""

    wei: int = 0
    i: int = 1
    while i <= 3:
        print(f"Day {i} harvest: ", end="")
        wei += int(input())
        i += 1
    print(f"Total harvest: {wei}")
