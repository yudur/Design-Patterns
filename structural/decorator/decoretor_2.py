from __future__ import annotations

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List
from copy import deepcopy


# Ingredients
@dataclass
class Ingredient:
    price: float

    
@dataclass
class Bread(Ingredient):
    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    price: float = 4.95


@dataclass
class Bacon(Ingredient):
    price: float = 6.77


@dataclass
class Egg(Ingredient):
    price: float = 1.50


@dataclass
class Cheese(Ingredient):
    price: float = 2.00


@dataclass
class MashedPotatoes(Ingredient):
    price: float = 2.25


@dataclass
class potatoSticks(Ingredient):
    price: float = 0.99


# Hotdogs
class Hotdog:
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name}({self.price}) -> {self.ingredients})'


class SimpleHotdog(Hotdog):
    def __init__(self) -> None:
        self._name: str = 'SimpleHotdog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            potatoSticks()
        ]


class SpecialHotdog(Hotdog):
    def __init__(self) -> None:
        self._name: str = 'SpecialHotdog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            Cheese(),
            MashedPotatoes(),
            potatoSticks()
        ]


# Decorators
class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog, ingredient: Ingredient) -> None:
        self.hotdog = hotdog
        self.ingredient = ingredient

        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self.ingredient)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self.ingredient.__class__.__name__}'


if __name__ == '__main__':
    simple_hotdog = SimpleHotdog()
    bacon_simple_hotdog = HotdogDecorator(simple_hotdog, Bacon())
    egg_bacon_simple_hotdog = HotdogDecorator(bacon_simple_hotdog, Egg())

    print(simple_hotdog)
    print(bacon_simple_hotdog)
    print(egg_bacon_simple_hotdog)
