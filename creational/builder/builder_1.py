from abc import ABC, abstractmethod
from typing import List


class StringRaprMixin:
    def __str__(self) -> str:
        params: str = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__} ( {params} )'

    def __repr__(self) -> str:
        return self.__str__()


class User(StringRaprMixin):
    def __init__(self) -> None:
        self.first_name = None
        self.last_name = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): pass

    @abstractmethod
    def add_firstname(self, first_name: str): pass

    @abstractmethod
    def add_last_name(self, last_name: str): pass

    @abstractmethod
    def add_age(self, age: int): pass

    @abstractmethod
    def add_phones(self, phone_numbers: List[str]): pass

    @abstractmethod
    def add_addresses(self, addresses: List[str]): pass


class UserBuilder(IUserBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def add_firstname(self, first_name: str):
        self._result.first_name = first_name
        return self

    def add_last_name(self, last_name: str):
        self._result.last_name = last_name
        return self

    def add_age(self, age: int):
        self._result.age = age
        return self

    def add_phones(self, phone_numbers: List[str]):
        self._result.phone_numbers.append(phone_numbers)
        return self
    
    def add_addresses(self, addresses: List[str]):
        self._result.addresses.append(addresses)
        return self


class UserDirector:
    def  __init__(self, builder: UserBuilder) -> None:
        self._builder: UserBuilder = builder

    def with_age(self, firstname, lastname, age):
        self._builder\
            .add_firstname(firstname)\
            .add_last_name(lastname)\
            .add_age(age)
        return self._builder.result

    def with_addresses(self, firstname, lastname, address):
        self._builder\
            .add_firstname(firstname)\
            .add_last_name(lastname)\
            .add_addresses(address)
        return self._builder.result



if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    
    user_1 = user_director.with_age('Yudi', 'Duarte', 13)
    user_2 = user_director.with_addresses('Joãozinho', 'Mendes', 'Rua Candida Duarte')

    print(user_1)
    print(user_2)