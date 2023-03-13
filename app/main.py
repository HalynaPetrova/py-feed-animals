class Animal:
    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True
                 ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> str:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.appetite > 0 and self.is_hungry is not False:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = not self.is_hungry
            return self.appetite
        return 0


class Cat(Animal):
    def __init__(self,
                 name: str,
                 appetite: int = 3,
                 is_hungry: bool = True
                 ) -> None:
        super().__init__(name, appetite, is_hungry)
        self.name = name
        self.is_hungry = is_hungry

    @staticmethod
    def catch_mouse() -> str:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self,
                 name: str,
                 appetite: int = 7,
                 is_hungry: bool = True
                 ) -> None:
        super().__init__(name, appetite, is_hungry)
        self.name = name
        self.is_hungry = is_hungry

    @staticmethod
    def bring_slippers() -> str:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    return sum([Animal.feed(animal) for animal in animals])
