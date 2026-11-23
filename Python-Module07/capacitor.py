from ex1 import (
    HealCapability,
    TransformCapability,
    HealingCreatureFactory,
    TransformCreatureFactory,
)


def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    base = factory.create_base()
    print(f"base: {base.describe()}")
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal())
    evolved = factory.create_evolved()
    print(f"evolved: {evolved.describe()}")
    print(evolved.attack())
    if isinstance(evolved, HealCapability):
        print(evolved.heal())


def test_transform(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    base = factory.create_base()
    print(f"base: {base.describe()}")
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
        print(base.attack())
        print(base.revert())
    evolved = factory.create_evolved()
    print(f"evolved: {evolved.describe()}")
    print(evolved.attack())
    if isinstance(evolved, TransformCapability):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


if __name__ == "__main__":
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()
    test_healing(healing)
    test_transform(transform)
