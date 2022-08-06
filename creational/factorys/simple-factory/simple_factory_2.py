# Simple Factory (criação)

from abc import abstractmethod
from random import choice


class Veiculo:
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('carro de luxo esta buscando o cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('carro popular esta buscando o cliente...')


class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto esta buscando o cliente...')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de Luxo esta buscando o cliente...')


class VeiculoFactory:
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()

        if tipo == 'popular':
            return CarroPopular()

        if tipo == 'moto':
            return Moto()

        if tipo == 'motoluxo':
            return MotoLuxo()

        assert 0, 'Veículo não existe'

    def buscar_cliente(self):
        self.carro.buscar_cliente()


if __name__ == '__main__':
    from random import choice

    carros_disponineis = ['luxo', 'popular', 'moto', 'motoluxo']

    for i in range(10):
        carro = VeiculoFactory(choice(carros_disponineis))
        carro.buscar_cliente()
