def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    try:
        print("Initiating secure vault access...")

        with open("classified_data.txt", "r") as file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            for line in file:
                print(line, end="")

        with open("security_protocols.txt", "w") as file:
            print("\n\nSECURE PRESERVATION:")
            security = "[CLASSIFIED] New security protocols archived"
            print(security)
            file.write(security)

        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
