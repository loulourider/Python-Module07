from abc import ABC, abstractmethod


class Creatures(ABC):
    def __init__(self, name: str, crea_type: str) -> None:
        self.name = name
        self.crea_type = crea_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.crea_type} type Creature"


class Flameling(Creatures):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creatures):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creatures):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creatures):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"
