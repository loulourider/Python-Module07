from ex0 import Creatures, CreatureFactory
from .creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creatures:
        return Sproutling()

    def create_evolved(self) -> Creatures:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creatures:
        return Shiftling()

    def create_evolved(self) -> Creatures:
        return Morphagon()
