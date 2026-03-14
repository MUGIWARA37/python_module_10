def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args):
        return (spell1(*args), spell2(*args))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args):
        return base_spell(*args) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def cast(*args):
        if condition(*args):
            return spell(*args)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args):
        return [spell(*args) for spell in spells]
    return sequence


if __name__ == "__main__":
    try:

        def fireball(target: str) -> str:
            return f"Fireball hits {target}"

        def heal(target: str) -> str:
            return f"Heals {target}"

        print("Testing spell combiner...")
        combined = spell_combiner(fireball, heal)
        result = combined("Dragon")
        print(f"Combined spell result: {result[0]}, {result[1]}")

        def damage(target: str) -> int:
            return 10

        print("\nTesting power amplifier...")
        mega = power_amplifier(damage, 3)
        print(f"Original: {damage('enemy')}, Amplified: {mega('enemy')}")

    except Exception as e:
        print(f"Error: {e}")
