def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    name_lost = "lost_archive.txt"
    name_class = "classified_data.txt"
    name_stan = "standard_archive.txt"
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
    except (PermissionError, FileNotFoundError):
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    try:
        print(f"\nROUTINE ACCESS: Attempting access to '{name_stan}'...")
        with open(name_stan, "r") as file:
            print("SUCCESS: Archive recovered - ``", end="")
            for line in file:
                print(line, end="\'\'")
            print("\nSTATUS: Normal operations resumed")
    except Exception as e:
        print(f"Unexpected error: {e}")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
