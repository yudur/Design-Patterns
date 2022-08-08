from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Colleague(ABC):
    def __init__(self) -> None:
        self.name: str

    @abstractmethod
    def broadcast(self, message: str) -> None: pass

    @abstractmethod
    def direct(self, message: str) -> None: pass


class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broadcast(self, message: str) -> None:
        self.mediator.broadcast(self, message)

    def direct(self, message: str) -> None:
        print(message)

    def send_direct(self, receiver: str, msg: str) -> None:
        self.mediator.direct(self, receiver, msg)


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague: Colleague, msg: str) -> None: pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str): pass


class Chatroom(Mediator):
    def __init__(self) -> None:
        self.colleagues: List[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues

    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, msg: str) -> None:
        if not self.is_colleague(colleague):
            return

        print(f'{colleague.name} disse: {msg}')

    def direct(self, sender: Colleague, receiver: str, msg: str):
        if not self.is_colleague(sender):
            return

        receiver_obj: List[Colleague] = [c for c in self.colleagues if c.name == receiver]  # c == colleague

        if not receiver_obj:
            return

        receiver_obj[0].direct(
            f'{sender.name} para {receiver_obj[0].name}: {msg}'
        )


if __name__ == '__main__':
    # mediator
    chat = Chatroom()

    # persons
    maria = Person('Maria', chat)
    ana = Person('Ana', chat)
    yudi = Person('Yudi', chat)
    jose = Person('José', chat)

    # adding the objects to the chat (Person)
    chat.add(maria)
    chat.add(ana)
    chat.add(yudi)
    # chat.add(jose)

    # global messages
    maria.broadcast('Olá pessoal!')
    ana.broadcast('Olá Maria!')
    jose.broadcast('Eu não fui adicionado ao chat...')

    print()
    
    # message from one object to another
    ana.send_direct('Yudi', 'Oi tudo bem?')
    yudi.send_direct('Ana', 'Tudo bem! E você?')