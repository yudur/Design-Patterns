from copy import deepcopy

class StringRaprMixin:
    def __str__(self) -> str:
        params: str = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__} ( {params} )'

    def __repr__(self) -> str:
        return self.__str__()


class Person(StringRaprMixin):
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses = []

    def add_address(self, address):
        self.addresses.append(address)

    def clone(self):
       return deepcopy(self)

class Address(StringRaprMixin):
    def __init__(self, street, number) -> None:
        self.street = street
        self.number = number


if __name__ == '__main__':
    marcos = Person('Marcos', 'Silva')
    address_marcos = Address('AV. Brasil', '250')
    marcos.add_address(address_marcos)

    esposa_marcos = marcos.clone()
    esposa_marcos.firstname = 'Maria'

    print(marcos)
    print(esposa_marcos)
