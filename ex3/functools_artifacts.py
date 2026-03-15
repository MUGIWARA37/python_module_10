import functools
import operator
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: a if a > b else b,
        "min": lambda a, b: a if a < b else b,
    }
    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": functools.partial(
            base_enchantment, power=50, element="Fire"
        ),
        "ice_enchant": functools.partial(
            base_enchantment, power=50, element="Ice"
        ),
        "lightning_enchant": functools.partial(
            base_enchantment, power=50, element="Lightning"
        ),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def cast(spell: Any) -> str:
        return f"Unknown spell type: {type(spell)}"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell dealing {spell} points"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {', '.join(str(s) for s in spell)}"

    return cast


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")

    print("\nTesting partial enchanter...")

    def base_enchantment(target: str, power: int, element: str) -> str:
        return f"{element} enchantment on {target} with power {power}"

    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire_enchant"](target="Sword"))
    print(enchanters["ice_enchant"](target="Shield"))
    print(enchanters["lightning_enchant"](target="Staff"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Fib(30): {memoized_fibonacci(30)}")

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("Fireball"))
    print(cast(["Heal", "Shield", "Haste"]))
