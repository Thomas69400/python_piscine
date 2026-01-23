"""Small CLI utility to compute basic statistics on integer scores."""
import sys
from typing import List


def main() -> None:
    """Execute program that reads scores from argv and prints analytics."""

    print("=== Player Score Analytics ===")
    if len(sys.argv) <= 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py " +
            "<score1> <score2> ...")
    else:
        scores: List[int] = []
        for a in sys.argv[1:]:
            try:
                scores.append(int(a))
            except ValueError:
                print(f"Oops, I typed '{a}' instead of a number")
                return
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores)/len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
