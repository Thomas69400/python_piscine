"""Data recovery system demo for reading an ancient fragment file.

Attempts to open and read a file, demonstrating FileNotFoundError handling.
"""


def main() -> None:
    """Execute data recovery routine.

    Reads and prints the contents of an archive file if present. Returns None.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    name: str = "ancient_fragment.txt"
    try:
        print(f"Accessing Storage Vault: {name}")
        with open(name, "r") as fd:
            print("\nConnection established...\n")
            data = fd.read()
            print("RECOVERED DATA:")
            print(data)
            print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
