# Factory Method (Criação)

from abc import abstractmethod, ABC
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


class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str): pass
        

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
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


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'popular':
            return CarroPopular()

        assert 0, 'Veículo não existe'


if __name__ == '__main__':
    from random import choice
    import colorama

    carros_disponineis_zona_norte = ['luxo', 'popular', 'moto', 'motoluxo']
    carros_disponineis_zona_sul = ['popular']

    print (colorama.Fore.GREEN  +  'ZONA NORTE' + colorama.Fore.RESET)

    for i in range(10):
        carro = ZonaNorteVeiculoFactory(choice(carros_disponineis_zona_norte))
        carro.buscar_cliente()

    print()

    print ( colorama.Fore.GREEN  +  'ZONA SUL' + colorama.Fore.RESET )

    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(choice(carros_disponineis_zona_sul))
        carro2.buscar_cliente()
