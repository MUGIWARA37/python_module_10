def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def cast(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


if __name__ == "__main__":
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
