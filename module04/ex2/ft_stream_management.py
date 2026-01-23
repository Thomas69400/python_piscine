"""Communication system demonstration.

Shows use of stdout/stderr together with user input to simulate
a three-channel communication test.
"""

import sys


def main() -> None:
    """Execute communication system demo.

    Prompts for an archivist ID and a status message, then writes to
    stdout and stderr. Returns None.
    """

    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    try:
        archiv_id: str = input("Input Stream active. Enter archivist ID: ")
        status: str = input("Input Stream active. Enter status report: ")
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
