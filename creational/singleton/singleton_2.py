from typing import Any, Callable


def singleton(the_class: Callable) -> Callable:
    instances: dict = {}

    def get_class(*args: Any, **kwargs: Any):
        if the_class not in instances:
            instances[the_class]: Callable = the_class(*args, **kwargs)
        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    def __init__(self) -> None:
        self.tema = 'tema escuro'
        self.font = '14px'


@singleton
class Teste:
    def __init__(self) -> None:
        print('oi')


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'claro'
    print(as1.tema)
    
    as2 = AppSettings()
    print(as1.tema)

    print(as1 == as2)

    print()


    t1 = Teste()
    t2 = Teste()
    print(t1 == t2)

    """
    Retorno:
    claro
    claro
    True

    True
    """
