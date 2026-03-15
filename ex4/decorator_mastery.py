import functools
import time


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            power = kwargs.get("power") or (args[1] if len(args) > 1 else None)
            if power is None or power < min_power:
                return "Insufficient power for this spell"
            return func(self, *args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c == " " for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting power validator...")

    @power_validator(min_power=20)
    def ice_lance(self, spell_name: str, power: int) -> str:
        return f"Cast {spell_name} with {power} power"

    class TestMage:
        cast = ice_lance

    mage = TestMage()
    print(mage.cast("Ice Lance", 25))
    print(mage.cast("Ice Lance", 5))

    print("\nTesting retry spell...")

    attempt_count = {"n": 0}

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        attempt_count["n"] += 1
        if attempt_count["n"] < 3:
            raise RuntimeError("Spell unstable!")
        return "Unstable spell succeeded!"

    print(unstable_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("X2"))
    print(guild.cast_spell("Lightning", power=15))
    print(guild.cast_spell("Lightning", power=5))
