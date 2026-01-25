"""Simple demonstration script for file-access error handling scenarios.

This module simulates attempts to access various archive files and prints
status messages to demonstrate handling of FileNotFoundError, PermissionError,
and generic exceptions.
"""


def main() -> None:
    """Simulate crisis archive accesses and print status messages.

    Attempts to open three different archive files demonstrating different
    exception handling branches. No return value.
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    name_lost: str = "lost_archive.txt"
    name_class: str = "classified_vault.txt"
    name_stan: str = "standard_archive.txt"

    try:
        print(f"CRISIS ALERT: Attempting access to '{name_lost}'...")
        with open(name_lost, "r") as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    try:
        print(f"\nCRISIS ALERT: Attempting access to '{name_class}'...")
        with open(name_class, "r") as file:
            print("SUCCESS: Vault opened - ", end="")
            for line in file:
                print(line)
    except FileNotFoundError:
        print(f"RESPONSE: Archive {name_class} not found")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    try:
        print(f"\nROUTINE ACCESS: Attempting access to '{name_stan}'...")
        with open(name_stan, "r") as file:
            print(f"SUCCESS: Archive recovered - ``{file.read()}``", end="")
            print("\nSTATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"RESPONSE: Archive {name_stan} not found")
        print("STATUS: Crisis handled, system stable")
    except Exception as e:
        print(f"Unexpected error: {e}")
        print("STATUS: Crisis contained")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
