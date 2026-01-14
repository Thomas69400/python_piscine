import sys
import math


def parse(to_parse: str) -> tuple:
    """Transform an argument string to an int

    Args:
        to_parse (str): the argument to transform

    Raises:
        ValueError: if cannot transform the argument in int

    Returns:
        tuple: the point created
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


def calculate_distance(t1: tuple, t2: tuple) -> float:
    """Calculate the distance between 2 points

    Args:
        t1 (tuple): coordinate of first point
        t2 (tuple): coordinate of second point

    Returns:
        float: the distance between the 2 points
    """

    return math.sqrt((t2[0]-t1[0])**2 + (t2[1]-t1[1])**2 + (t2[2]-t1[2])**2)


if __name__ == "__main__":
    """Execute program"""

    print("=== Game Coordinate System ===\n")
    spawn = tuple((0, 0, 0))
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
