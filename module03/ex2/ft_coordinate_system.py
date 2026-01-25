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

    parts = to_parse.split(",")
    return (int(parts[0]), int(parts[1]), int(parts[2]))


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


def main() -> None:
    """Execute the coordinate system demonstration."""
    print("=== Game Coordinate System ===\n")

    origin: Tuple[int, int, int] = (0, 0, 0)

    pos1: Tuple[int, int, int] = (10, 20, 5)
    print(f"Position created: {pos1}")
    dist1 = calculate_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {dist1:.2f}")

    if len(sys.argv) == 2:
        print(f"\nParsing coordinates: \"{sys.argv[1]}\"")
        try:
            pos2 = parse(sys.argv[1])
            dist2 = calculate_distance(origin, pos2)
            print(f"Distance between {origin} and {pos2}: {dist2}")
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")

    print("\nParsing coordinates: \"3,4,0\"")
    try:
        pos2 = parse("3,4,0")
        print(f"Parsed position: {pos2}")
        dist2 = calculate_distance(origin, pos2)
        print(f"Distance between {origin} and {pos2}: {dist2}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")

    print("\nParsing invalid coordinates: \"abc,def,ghi\"")
    try:
        parse("abc,def,ghi")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("\nUnpacking demonstration:")
    x, y, z = pos2
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
