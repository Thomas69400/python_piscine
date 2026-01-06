def main():
    name = "new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    try:
        print(f"Initializing new storage unit: {name}")
        fd = open(name, "a")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        print("[ENTRY 001] New quantum algorithm discovered")
        fd.write("[ENTRY 001] New quantum algorithm discovered\n")
        print("[ENTRY 002] Efficiency increased by 347%")
        fd.write("[ENTRY 002] Efficiency increased by 347%\n")
        print("[ENTRY 003] Archived by Data Archivist trainee")
        fd.write("[ENTRY 003] Archived by Data Archivist trainee\n")
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{name}.txt' ready for long-term preservation.")


if __name__ == "__main__":
    main()
