"""Recursive countdown until harvest prompt example."""
from typing import Optional


def ft_count_harvest_recursive(n: Optional[int] = None, day: int = 1) -> None:
    """Recursively print each day until harvest.

    If n is None, prompts the user for the number of days to count.
    Args:
        n (Optional[int]): Total number of days to wait until harvest.
        day (int): Current day counter (starts at 1).
    """
    if n is None:
        print("Days until harvest: ", end="")
        n = int(input())  # type: int
    if day > n:
        print("Harvest time!")
        return
    print(f"Day {day}")
    ft_count_harvest_recursive(n, day + 1)
