from abc import ABC, abstractmethod
from typing import List


class Handler(ABC):
    def __init__(self) -> None:
        self.sucessor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str: pass


class HandlerABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters: List[str] = ['A', 'B', 'C']
        self.sucessor: Handler = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'{__class__.__name__}: conseguiu tratar o valor {letter}'

        return self.sucessor.handle(letter)


class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters: List[str] = ['D', 'E', 'F']
        self.sucessor: Handler = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'{__class__.__name__}: conseguiu tratar o valor {letter}'

        return self.sucessor.handle(letter)


class HandlerGHI(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters: List[str] = ['G', 'H', 'I']
        self.sucessor: Handler = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'{__class__.__name__}: conseguiu tratar o valor {letter}'

        return self.sucessor.handle(letter)


class HandleUnsolved(Handler):
    def handle(self, letter: str) -> str:
        return f'{__class__.__name__}: não conseguiu tratar o valor {letter}'


if __name__ == '__main__':
    handle_unsolved = HandleUnsolved()
    handleghi = HandlerGHI(handle_unsolved)
    handledef = HandlerDEF(handleghi)
    handleabc = HandlerABC(handledef)

    print(handleabc.handle('A'))
    print(handleabc.handle('B'))
    print(handleabc.handle('C'))
    print(handleabc.handle('D'))
    print(handleabc.handle('E'))
    print(handleabc.handle('F'))
    print(handleabc.handle('G'))
    print(handleabc.handle('H'))
    print(handleabc.handle('I'))
    print(handleabc.handle('J'))
    print(handleabc.handle('K'))
    print(handleabc.handle('L'))

    print()

    print(handledef.handle('B'))
    print(handledef.handle('C'))
    print(handledef.handle('D'))
    print(handledef.handle('A'))
    print(handledef.handle('E'))
    print(handledef.handle('F'))
    print(handledef.handle('G'))
    print(handledef.handle('H'))
    print(handledef.handle('I'))
    print(handledef.handle('J'))
    print(handledef.handle('K'))
    print(handledef.handle('L'))

    print()

    print(handleghi.handle('D'))
    print(handleghi.handle('C'))
    print(handleghi.handle('B'))
    print(handleghi.handle('A'))
    print(handleghi.handle('E'))
    print(handleghi.handle('F'))
    print(handleghi.handle('G'))
    print(handleghi.handle('H'))
    print(handleghi.handle('I'))
    print(handleghi.handle('J'))
    print(handleghi.handle('K'))
    print(handleghi.handle('L'))    

    print()

    print(handle_unsolved.handle('D'))
    print(handle_unsolved.handle('C'))
    print(handle_unsolved.handle('B'))
    print(handle_unsolved.handle('A'))
    print(handle_unsolved.handle('E'))
    print(handle_unsolved.handle('F'))
    print(handle_unsolved.handle('G'))
    print(handle_unsolved.handle('H'))
    print(handle_unsolved.handle('I'))
    print(handle_unsolved.handle('J'))
    print(handle_unsolved.handle('K'))
    print(handle_unsolved.handle('L'))