# Factory Method (Criação)

from abc import abstractmethod, ABC
from typing import Callable


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('carro de luxo ZS esta buscando o cliente...')


class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('carro popular ZS esta buscando o cliente...')


class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto ZS esta buscando o cliente...')


class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de Luxo ZS esta buscando o cliente...')
        

class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('carro de luxo ZN esta buscando o cliente...')


class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('carro popular ZN esta buscando o cliente...')


class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto ZN esta buscando o cliente...')


class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de Luxo ZN esta buscando o cliente...')


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_luxo(tipo: str) -> VeiculoLuxo: pass

    @staticmethod
    @abstractmethod
    def get_carro_popular(tipo: str) -> VeiculoPopular: pass

    @staticmethod
    @abstractmethod
    def get_moto_luxo(tipo: str) -> VeiculoLuxo: pass

    @staticmethod
    @abstractmethod
    def get_moto_popular(tipo: str) -> VeiculoPopular: pass


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()
    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZN()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZN()


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()
    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZS()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZS()


class Filial:
    def variables(self, factoryveiculo: Callable) -> None:
        for factory in [factoryveiculo()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_popular()
            carro_luxo.buscar_cliente()
            
            moto_popular = factory.get_carro_popular()
            moto_popular.buscar_cliente()
            
            moto_luxo = factory.get_carro_popular()
            moto_luxo.buscar_cliente()


    def busca_clientes_zn(self) -> None:
        self.variables(ZonaNorteVeiculoFactory)

    
    def busca_clientes_zs(self) -> None:
        self.variables(ZonaSulVeiculoFactory)


if __name__ == '__main__':
    filial = Filial()
    filial.busca_clientes_zn()

    print()

    filial.busca_clientes_zs()
