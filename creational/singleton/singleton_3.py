from typing import Any, Callable


# class Meta(type):
#     def __call__(cls, *args: Any, **kwargs: Any) -> Callable:
#         print('CALL é executado')
#         return super().__call__(*args, **kwargs)


# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args: Any, **kwargs: Any):
#         print('NEW é executado')
#         return super().__new__(cls)

#     def __init__(self, nome: str) -> None:
#         print('INIT é executado')
#         self.nome: str = nome

#     def __call__(self):
#             print ('call chamado')


# p1 = Pessoa('Yudi')
# print(p1.nome)

class Singleton(type):
    _instaces: dict = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instaces:
            cls._instaces[cls] = super().__call__(*args, **kwds)
        return cls._instaces[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        self.tema = 'tema escuro'
        self.font = '14px'


if __name__ == "__main__":
    as1 = AppSettings()
    
    as1.tema = 'tema amarelo'

    as2 = AppSettings()
    as3 = AppSettings()

    print(as3.tema)

    print()

    print(as1 == as2)
    print(as1 == as3)
    print(as2 == as3)

    """
    Retorno:
    tema amarelo

    True
    True
    True
    """