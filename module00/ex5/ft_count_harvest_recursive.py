def ft_count_harvest_recursive(n=None, day=1):
    if n is None:
        print("Days until harvest: ", end="")
        n = int(input())
    if day > n:
        print("Harvest time!")
        return
    print(f"Day {day}")
    ft_count_harvest_recursive(n, day + 1)
