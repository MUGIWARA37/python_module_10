def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    total = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, callable]:
    storage = {}

    def store(key: str, value) -> None:
        storage[key] = value

    def recall(key: str):
        return storage.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {counter()}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']('spell1', 'Fireball')
    print(vault['recall']('spell1'))
    print(vault['recall']('spell2'))