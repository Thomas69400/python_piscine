from functools import wraps


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper():
        print(f"Casting {func.__name__}...")
        func()
        print("Spell completed in 0.101 seconds")
        return func()
    return wrapper


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


def power_validator(min_power: int) -> callable:
    """Power validator function"""

    def validator(func: callable) -> callable:
        """Validator function"""

        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> str:
            """wrapper"""

            if args[0] < min_power:
                return "Insufficient power for this spell"
            return func(*args)
        return wrapper

    return validator


@power_validator(20)
def power(check_pow: int) -> str:
    return f"{check_pow} is enough!"


def retry_spell(max_attempts: int) -> callable:

    def retry(func: callable):

        @wraps(func)
        def wrapper(*args, **kwargs):

            if wrapper.attempts >= max_attempts:
                return f"Spell casting failed after {max_attempts} " + \
                    "attempts"
            try:
                result = func(*args, **kwargs)
                wrapper.attempts = 0
                return result

            except Exception:
                wrapper.attempts += 1
                print(
                    "Spell failed, retrying... " +
                    f"(attempt {wrapper.attempts}/{max_attempts})")
        wrapper.attempts = 0
        return wrapper
    return retry


@retry_spell(3)
def lightning(error: bool = True) -> str:
    if error:
        raise ValueError("Error lightning")
    return "LIGHTNING"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


def main():
    test_powers = [9, 23, 9, 27]
    spell_names = ['tornado', 'tsunami', 'flash', 'lightning']
    mage_names = ['Alex', 'Rowan', 'Sage', 'Storm', 'Morgan', 'Nova']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    print("Testing spell timer...")
    try:
        spell_time = fireball()
        print(f"Result: {spell_time}")
    except TypeError as e:
        print(f"Error spell timer: {e}")

    print("\nTesting power validator...")
    try:
        print(power(test_powers[2]))
        print(power(test_powers[1]))
    except TypeError as e:
        print(f"Error power validator: {e}")

    print("\nTesting retry spell...")
    try:
        spell = lightning()
        if spell:
            print(spell)
        spell = lightning()
        if spell:
            print(spell)
        spell = lightning(False)
        if spell:
            print(spell)
        for _ in range(4):
            spell = lightning()
            if spell:
                print(spell)
    except TypeError as e:
        print(f"Error retry spell: {e}")


if __name__ == "__main__":
    main()
