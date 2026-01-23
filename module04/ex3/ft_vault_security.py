"""Vault security utilities demo.

This module demonstrates reading a classified archive and writing new
security protocols to disk while handling exceptions.
"""


def main() -> None:
    """Execute vault access and preservation operations.

    Reads a classified file and writes security protocols to a new file.
    Returns None.
    """

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
            security: str = "[CLASSIFIED] New security protocols archived"
            print(security)
            file.write(security)

        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
