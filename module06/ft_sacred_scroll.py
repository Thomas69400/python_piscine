"""Demo script exercising the public API of the alchemy package.

Calls element-creation helpers and prints package metadata.
"""

import alchemy
import alchemy.elements

if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    try:
        result: str = alchemy.elements.create_fire()
        print("alchemy.elements.create_fire(): " +
              f"{result}")
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        result: str = alchemy.elements.create_water()
        print("alchemy.elements.create_water(): " +
              f"{result}")
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        result: str = alchemy.elements.create_earth()
        print("alchemy.elements.create_earth(): " +
              f"{result}")
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        result: str = alchemy.elements.create_air()
        print(
            f"alchemy.elements.create_air(): {result}")
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        result: str = alchemy.create_fire()
        print("alchemy.create_fire(): ", end="")
        print(result)
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        result: str = alchemy.create_water()
        print("alchemy.create_water(): ", end="")
        print(result)
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        result: str = alchemy.created_earth()
        print("alchemy.create_earth(): ", end="")
        print(result)
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        result: str = alchemy.created_air()
        print("alchemy.create_air(): ", end="")
        print(result)
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nPackage metadata: ")
    version: str = alchemy.__version__
    author: str = alchemy.__author__
    print(f"Version: {version}")
    print(f"Author: {author}")
