def ft_count_harvest_iterative():
    print("Days until harvest: ", end="")
    days = int(input())
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")
