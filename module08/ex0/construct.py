"""Utility to display information about the current Python virtual environment.

This module prints guidance to the user about entering/creating a virtual
environment and displays the current Python executable and environment path
when a virtual environment is active.
"""

import sys
import os
from typing import Optional


def main() -> None:
    """Display virtual environment status and instructions.

    - If VIRTUAL_ENV is not set, prints instructions to create/activate a venv
      and warns about using the global environment.
    - If VIRTUAL_ENV is set, prints details about the active environment and
      a typical site-packages path for package installation.

    Returns:
        None
    """
    env: Optional[str] = os.getenv("VIRTUAL_ENV")
    if not env:
        print("MATRIX STATUS: You're still plugged in\n")
        python_exec: str = sys.executable
        print(f"Current Python: {python_exec}\n")

        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment! " +
              "The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows\n")

        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct\n")
        python_exec: str = sys.executable
        env_name: str = env.split(os.sep)[-1]
        site_packages: str = f"{env}/lib/python3.11/site-packages"
        print(f"Current Python: {python_exec}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env}")
        print("\nSUCCESS You're in an isolated environment! " +
              "Safe to install packages without affecting " +
              "the global system.")
        print("\nPackage installation path:")
        print(site_packages)


if __name__ == "__main__":
    main()
