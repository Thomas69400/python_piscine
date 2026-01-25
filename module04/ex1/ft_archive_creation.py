"""Preservation system demo for creating a new archive file.

Creates a new text archive, writes several entries, and prints status
messages. Intended to show safe file creation and writing.
"""


def main() -> None:
    """Execute archive creation routine.

    Creates a new archive file and writes several entries. Returns None.
    """
    name: str = "new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    try:
        print(f"Initializing new storage unit: {name}")
        with open(name, "w") as fd:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            print("[ENTRY 001] New quantum algorithm discovered")
            fd.write("[ENTRY 001] New quantum algorithm discovered\n")
            print("[ENTRY 002] Efficiency increased by 347%")
            fd.write("[ENTRY 002] Efficiency increased by 347%\n")
            print("[ENTRY 003] Archived by Data Archivist trainee")
            fd.write("[ENTRY 003] Archived by Data Archivist trainee\n")
            print("\nData inscription complete. Storage unit sealed.")
            print(f"Archive '{name}' ready for long-term preservation.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
