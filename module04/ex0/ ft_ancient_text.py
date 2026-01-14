def main():
    """Execute program"""

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    name = "ancient_fragment.txt"
    try:
        print(f"Accessing Storage Vault: {name}")
        with open(name, "r") as fd:
            print("\nConnection established...\n")
            data = fd.read()
            print("RECOVERED DATA:")
            print(data)
            print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError as e:
        print(f"ERROR: Storage vault not found {e}")


if __name__ == "__main__":
    main()
