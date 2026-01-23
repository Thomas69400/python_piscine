"""CLI example showing access to sys.argv and basic argument iteration."""
import sys


def main() -> None:
    """Execute Command Quest demonstrating argv traversal."""
    print("=== Command Quest ===")
    if len(sys.argv) <= 1:
        print("No arguments provided!")
        print(
            f"Program name: {sys.argv[0]}\nTotal arguments: {len(sys.argv)}")
    else:
        print(
            f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        i: int = 1
        while i <= len(sys.argv) - 1:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
