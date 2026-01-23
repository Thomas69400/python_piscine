"""Simple coordinate parsing and Euclidean distance utilities for demos."""
import sys
import math
from typing import Tuple


def parse(to_parse: str) -> Tuple[int, int, int]:
    """Parse a comma-separated string into a 3D coordinate tuple of ints.

    Args:
        to_parse (str): the argument to transform, e.g. "1,2,3"

    Raises:
        ValueError: if cannot transform the argument into three ints

    Returns:
        Tuple[int, int, int]: the parsed (x, y, z) point
    """

    nbr = to_parse.split(",")
    try:
        t = tuple((int(nbr[0]), int(nbr[1]), int(nbr[2])))
    except ValueError as e:
        raise ValueError(f"Parsing invalid coordinates: \"{to_parse}\"\n" +
                         f"Error parsing coordinates: {e}\n" +
                         f"Error details - Type: {e.__class__.__name__}, " +
                         f"Args: {e.args}")
    else:
        print(f"Parsing coordinates: \"{to_parse}\"")
        print(f"Parsed position: {t}")
        return t


def calculate_distance(t1: Tuple[int, int, int],
                       t2: Tuple[int, int, int]) -> float:
    """Calculate the Euclidean distance between two 3D points.

    Args:
        t1 (Tuple[int,int,int]): coordinate of first point
        t2 (Tuple[int,int,int]): coordinate of second point

    Returns:
        float: the distance between the two points
    """

    return math.sqrt((t2[0]-t1[0])**2 + (t2[1]-t1[1])**2 + (t2[2]-t1[2])**2)


if __name__ == "__main__":
    """Execute program"""

    print("=== Game Coordinate System ===\n")
    spawn: Tuple[int, int, int] = tuple((0, 0, 0))
    if len(sys.argv) <= 1:
        print("No arguments found : try with something like <int1,int2,int3>")
    else:
        try:
            t = parse(sys.argv[1])
        except ValueError as e:
            print(f"{e}")
        else:
            d = calculate_distance(spawn, t)
            print(f"Distance between {spawn} and {t}: {d:.2f}")
            print("\nUnpacking demonstration:")
            (x, y, z) = t
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}")
