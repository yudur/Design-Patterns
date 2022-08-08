from __future__ import annotations
from copy import deepcopy
from typing import Dict, Any, List


class Memento:
    def __init__(self, state: Dict) -> None:
        self._state: Dict
        super().__setattr__('_state', state)

    def get_state(self) -> Dict:
        return self._state

    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError('Descupa, eu sou imutavel :)')


class ImageEditor:
    def __init__(self, name: str, width: int, height: int) -> None:
        self.name = name
        self.width = width
        self.height = height

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'


class Caretaker:
    def __init__(self, originator: ImageEditor) -> None:
        self._originator: ImageEditor = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:
        if not self._mementos:
            return

        self._originator.restore(self._mementos.pop())

if __name__ == '__main__':
    img = ImageEditor('Imagem_1.png', 111, 111)
    caretaker = Caretaker(img)

    caretaker.backup()

    img.name = 'Imagem_1_alterada.png'
    img.height = 222
    img.width = 222
    caretaker.backup()

    img.name = 'Imagem_1_alterada_3.png'
    img.height = 333
    img.width = 333

    caretaker.restore()

    print(img)