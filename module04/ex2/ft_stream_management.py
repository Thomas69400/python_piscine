import sys


def main():
    """Execute program"""

    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    try:
        archiv_id = input("Input Stream active. Enter archivist ID: ")
        status = input("Input Stream active. Enter status report: ")
        print("")
        sys.stdout.write(f"[STANDARD] Archive status from {archiv_id}: " +
                         f"{status}\n")
        sys.stderr.write("[ALERT] System diagnostic: Communication " +
                         "channels verified\n")
        sys.stdout.write("[STANDARD] Data transmission complete\n")
        print("\nThree-channel communication test successful.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
