from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class BoxStructure(ABC):
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass
    def remove(self, child: BoxStructure) -> None: pass


class Box(BoxStructure):
    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        print(f'\n{self.name}:')

        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum(
            [
                child.get_price() for child in self._children
            ]
        )

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self._price = price

    def print_content(self) -> None:
        print(self.name, self._price)

    def get_price(self) -> float:
        return self._price


if __name__ == '__main__':
    camiseta1 = Product('Camiseta1', 15.88)
    camiseta2 = Product('Camiseta2', 44.90)
    camiseta3 = Product('Camiseta3', 20.43)
    camiseta4 = Product('Camiseta4', 19.99)

    caixa_camisetas = Box('Caixa de camisetas')

    caixa_camisetas.add(camiseta1)
    caixa_camisetas.add(camiseta2)
    caixa_camisetas.add(camiseta3)
    caixa_camisetas.add(camiseta4)

    smartphone1 = Product('smartphone1', 5000.00)
    smartphone2 = Product('smartphone2', 11000.00)

    caixa_smartphone = Box('Caixa de smartphones')

    caixa_smartphone.add(smartphone1)
    caixa_smartphone.add(smartphone2)

    caixa_grande = Box('Caixa grande')

    caixa_grande.add(caixa_camisetas)
    caixa_grande.add(caixa_smartphone)

    caixa_grande.print_content()
    print(caixa_grande.get_price())
