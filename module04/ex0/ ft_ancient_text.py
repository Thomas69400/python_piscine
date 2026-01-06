def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    name = "../ancient_fragment.txt"
    try:
        print(f"Accessing Storage Vault: {name}")
        fd = open(name, "r")
    except FileNotFoundError as e:
        print(f"ERROR: Storage vault not found {e}")
    else:
        print("\nConnection established...\n")
        data = fd.read()
        print("RECOVERED DATA:")
        print(data)
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
