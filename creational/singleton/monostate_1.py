from typing import Any, Callable


class StringRaprMixin:
    def __str__(self) -> str:
        params: str = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__} ( {params} )'

    def __repr__(self) -> str:
        return self.__str__()


class MonoState(StringRaprMixin):
    _state: dict = {'x': 12, 'y': 100}

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, nome: str|None = None , sobrenome: str|None = None) -> None:
        if nome is not None:
            self.nome: str = nome
        
        if sobrenome is not None:
            self.sobrenome: str = sobrenome


if __name__ == '__main__':
    m1 = MonoState(nome='Yudi')
    m2 = MonoState(sobrenome='Duarte')

    m1.x = 'qualque coisa'

    print(m1)
    print(m2)