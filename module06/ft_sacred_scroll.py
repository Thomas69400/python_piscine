import alchemy

if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    try:
        print("alchemy.elements.create_fire(): " +
              f"{alchemy.elements.create_fire()}")
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("alchemy.elements.create_water(): " +
              f"{alchemy.elements.create_water()}")
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("alchemy.elements.create_earth(): " +
              f"{alchemy.elements.create_earth()}")
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print(
            f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print("alchemy.elements.create_fire(): ", end="")
        print(alchemy.create_fire())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_water(): ", end="")
        print(alchemy.create_water())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_earth(): ", end="")
        print(alchemy.created_earth())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_air(): ", end="")
        print(alchemy.created_air())
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nPackage metadata: ")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")
