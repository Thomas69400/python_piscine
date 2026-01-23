def ft_water_reminder() -> None:
    """Prompt how many days since last watering and advise whether to water."""

    print("Days since last watering: ", end="")
    days: int = int(input())
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
