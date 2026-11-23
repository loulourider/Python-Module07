from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def creature_fight(
        factory1: CreatureFactory,
        factory2: CreatureFactory
        ) -> None:
    basew = factory1.create_base()
    basef = factory2.create_base()
    print("Testing battle")
    print(basef.describe())
    print(" vs.")
    print(basew.describe())
    print(" fight!")
    print(basef.attack())
    print(basew.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    test_factory(flame)
    print("\n")
    test_factory(aqua)
    print("\n")
    creature_fight(aqua, flame)
