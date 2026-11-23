from abc import ABC, abstractmethod

from .creatures import Creatures, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creatures:
        pass

    @abstractmethod
    def create_evolved(self) -> Creatures:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creatures:
        return Flameling()

    def create_evolved(self) -> Creatures:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creatures:
        return Aquabub()

    def create_evolved(self) -> Creatures:
        return Torragon()
