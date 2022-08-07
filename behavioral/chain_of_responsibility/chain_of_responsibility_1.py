# teoria com funções

def HandlerABC(letter: str) -> str:
    letters = ['A', 'B', 'C']

    if letter in letters:
        return f'Handler_ABC: conseguiu tratar o valor {letter}'

    return handler_DEF(letter)


def handler_DEF(letter: str) -> str:
    letters = ['D', 'E', 'F']

    if letter in letters:
        return f'Handler_DEF: conseguiu tratar o valor {letter}'

    return handle_unsolved(letter)


def handle_unsolved(latter: str) -> str:
    return f'handle_unsolver: não sei tratar {latter}'


if __name__ == '__main__':
    print(HandlerABC('A'))
    print(HandlerABC('B'))
    print(HandlerABC('C'))
    print(HandlerABC('D'))
    print(HandlerABC('E'))
    print(HandlerABC('F'))
    print(HandlerABC('G'))
    print(HandlerABC('H'))
    print(HandlerABC('I'))