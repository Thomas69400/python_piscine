def ft_harvest_total():
    """Ask user the day to wait to"""

    wei = 0
    i = 1
    while i <= 3:
        print(f"Day {i} harvest: ", end="")
        wei += int(input())
        i += 1
    print(f"Total harvest: {wei}")
