def ft_water_reminder():
    """Ask input to user and print if need water or not"""

    print("Days since last watering: ", end="")
    days = int(input())
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
