from __future__ import annotations
from typing import Dict, List


class Client:
    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []

        # extrinsic adress data
        self.address_number: str
        self.address_datails: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self. address_number, self.address_datails)


class Address:
    def __init__(self, street: str, neighbourhood: str, zip_code: str) -> None:
        self._street = street
        self._neighbourhood = neighbourhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_detail) -> None:
        print(
            self._street, address_number, address_detail, self._zip_code
        )

    
class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())

    def get_address(self, **kwargs):
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('Usando objeto já criado')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Criando novo objeto')

        return address_flyweight


if __name__ == '__main__':
    address_factory = AddressFactory()

    a1 = address_factory.get_address(
        street='Av. Brasil',
        neighbourhood='Centro',
        zip_code='000000-0000'
    )
    
    a2 = address_factory.get_address(
        street='Av. Brasil',
        neighbourhood='Centro',
        zip_code='000000-0000'
    )

    yudi = Client('Yudi')
    yudi.address_number = '100'
    yudi.address_datails = 'Casa'
    yudi.add_address(a1)
    yudi.list_addresses()

    joana = Client('Joana')
    joana.address_number = '32'
    joana.address_datails = 'Hotel 123'
    joana.add_address(a1)
    joana.list_addresses()