import sys


def main():
    """Main function"""

    print("=== Player Score Analytics ===")
    if len(sys.argv) <= 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py " +
            "<score1> <score2> ...")
    else:
        scores = []
        for a in sys.argv[1:]:
            try:
                scores.append(int(a))
            except ValueError:
                print(f"Oops, I typed '{a}' instead of a number")
                return
        print("Scores processed: [", end="")
        for s in scores:
            print(f"{s}", end="")
            if s != scores[-1]:
                print(", ", end="")
        print(f"]\nTotal Players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores)/len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
