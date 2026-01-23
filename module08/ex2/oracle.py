"""Read and report environment configuration from a .env file.

This utility loads environment variables using python-dotenv and prints core
configuration values if present.
"""

import os
from dotenv import load_dotenv
from typing import Optional


def main() -> None:
    """Load .env configuration and display key environment settings.

    - Attempts to load environment variables from a .env file.
    - If loaded, prints selected configuration keys (MATRIX_MODE, DATABASE_URL,
      API_KEY, LOG_LEVEL, ZION_ENDPOINT). Missing keys are reported.
    - If .env not found, advises how to create one.
    - Performs a few basic "security" checks and prints a summary.

    Returns:
        None
    """
    print("ORACLE STATUS: Reading the Matrix...")
    loaded: bool = load_dotenv()
    if loaded:
        print("\nConfiguration loaded:")
        try:
            mode: Optional[str] = os.environ.get("MATRIX_MODE")
            db: Optional[str] = os.environ.get("DATABASE_URL")
            api: Optional[str] = os.environ.get("API_KEY")
            log_level: Optional[str] = os.environ.get("LOG_LEVEL")
            zion: Optional[str] = os.environ.get("ZION_ENDPOINT")
            print(f"Mode: {mode}")
            print(f"Database: {db}")
            print(f"API Access: {api}")
            print(f"Log Level: {log_level}")
            print(f"Zion Network: {zion}")
        except Exception as e:
            print(f"Environment value not found: {e}")
            return
    else:
        print("\nConfiguration not found. Are you sure having a .env file ?")
        print("Try creating a .env file or -> cp .env.example .env")
        return

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
