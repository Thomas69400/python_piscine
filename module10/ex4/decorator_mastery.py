"""Decorators and utilities demonstrating decorator composition.

Provides timing, validation and retry decorators used by sample spell
functions and a MageGuild example. Type hints improved for wrappers.
"""
from functools import wraps
from typing import Any, Callable, Tuple, Dict


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that prints a cast timeline around function execution.

    The wrapper prints a start message, calls the function once and prints a
    completed message. Returns the wrapped function result.
    """
    @wraps(func)
    def wrapper(*args: Tuple[Any, ...],
                **kwargs: Dict[str, Any]) -> Any:
        """Wrapper that executes the function and prints timing messages."""
        print(f"Casting {func.__name__}...")
        result = func(*args, **kwargs)
        print("Spell completed in 0.101 seconds")
        return result
    return wrapper


@spell_timer
def fireball() -> str:
    """Cast a basic fireball spell and return a confirmation string."""
    return "Fireball cast!"


def power_validator(min_power: int) -> Callable[[Callable[..., Any]],
                                                Callable[..., Any]]:
    """Return a decorator that ensures integer power args meet min_power.

    The returned decorator inspects positional integer arguments and returns
    an error message string when any integer arg is below min_power.
    """
    def validator(func: Callable[..., Any]) -> Callable[..., Any]:
        """Validator decorator for a specific function."""
        @wraps(func)
        def wrapper(*args: Tuple[Any, ...],
                    **kwargs: Dict[str, Any]) -> Any:
            """Wrapper that inspects positional integer args for minimum
            power and forwards the call."""
            for arg in args:
                if isinstance(arg, int) and arg < min_power:
                    return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return validator


@power_validator(20)
def power(check_pow: int) -> str:
    """Return whether the provided integer power meets the validator level."""
    return f"{check_pow} is enough!"


def retry_spell(max_attempts: int) -> Callable[[Callable[..., Any]],
                                               Callable[..., Any]]:
    """Return a decorator that retries a function up to max_attempts on
    Exception.

    The wrapper keeps an attempts counter attribute and returns an error
    message after exceeding max_attempts.
    """
    def retry(func: Callable[..., Any]) -> Callable[..., Any]:
        """Decorator that wraps a callable with retry logic."""
        @wraps(func)
        def wrapper(*args: Tuple[Any, ...],
                    **kwargs: Dict[str, Any]) -> Any:
            """Wrapper that retries the wrapped function on exception."""
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return retry


@retry_spell(3)
def lightning(error: bool = True) -> str:
    """Simulate a lightning spell that may raise an error when `error`
    is True. Returns a string on success.
    """
    if error:
        raise ValueError("Error lightning")
    return "LIGHTNING"


class MageGuild:
    """Simple MageGuild example demonstrating validation on methods.

    Attributes:
        name: The guild member name.
    """

    def __init__(self, name: str) -> None:
        self.name: str = name

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True if name looks like a simple alphabetic mage name."""
        if len(name) < 3:
            return False
        for char in name:
            if not (char.isalpha() or char.isspace()):
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell if power is sufficient (validated by decorator)."""
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
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
    except TypeError as e:
        print(f"Error retry spell: {e}")

    print("\nTesting MageGuild...")
    try:
        is_name_valid: bool = MageGuild.validate_mage_name(mage_names[1])
        is_name_invalid: bool = MageGuild.validate_mage_name(invalid_names[1])
        print(is_name_valid)
        print(is_name_invalid)
        if is_name_valid:
            mage = MageGuild(mage_names[1])
            print(mage.cast_spell(spell_names[1], test_powers[1]))
            print(mage.cast_spell(spell_names[1], test_powers[2]))

    except TypeError as e:
        print(f"Error MageGuild: {e}")


if __name__ == "__main__":
    main()
