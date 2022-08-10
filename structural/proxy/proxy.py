from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import Dict, List


class IUser(ABC):
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> Dict: pass


class RealUser(IUser):
    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)  # simulando requisição
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        sleep(2)  # simulando requisição
        return [{'rua': 'Candida Duarte', 'numero': '1000'}]

    def get_all_user_data(self) -> Dict:
        sleep(2)  # simulando requisição
        return {'CPF': '444.444.444-44', 'RG': 'AB111222333'}

    
class UserProxy(IUser):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

        # Esses objetos ainda não existem nesse ponto do código
        self._real_user: RealUser
        self._cached_adresses: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)

    def get_addresses(self) -> List[Dict]:
        self.get_real_user()

        if not hasattr(self, '_cached_adresses'):
            self._cached_adresses = self._real_user.get_addresses()

        return self._cached_adresses

    def get_all_user_data(self) -> Dict:
        self.get_real_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()

        return self._all_user_data


if __name__ == '__main__':
    luiz = UserProxy('Luiz', 'Marquês')

    print(luiz.firstname, luiz.lastname)

    #  6 segundos
    print(luiz.get_all_user_data())
    print(luiz.get_addresses())

    print()

    # resposta instantaniamente
    print('Cache data:')
    for i in range(50):
        print(luiz.get_addresses())