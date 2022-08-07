from abc import ABC, abstractmethod
from typing import Any


class Pizza(ABC):
    def prapare(self) -> None:
        """ Template Method """
        self.hook_before_add_ingrentients()  # hook
        self.add_ingrentients()  # abstract
        self.hook_after_add_ingrentients()  # hook

        self.hook_before_cook()  # hook
        self.cook()  # abstract
        self.hook_after_cook()  # hook

        self.cut()  # concrete
        self.serve()  # concrete
    
    def hook_before_add_ingrentients(self) -> Any: pass
    def hook_after_add_ingrentients(self) -> Any: pass

    def hook_before_cook(self) -> Any: pass
    def hook_after_cook(self) -> Any: pass



    @abstractmethod
    def add_ingrentients(self) -> Any: pass

    @abstractmethod
    def cook(self) -> Any: pass
    
    def cut(self) -> None:
        print(f'{self.__class__.__name__}: CORTADA')

    def serve(self) -> None:
        print(f'{self.__class__.__name__}: SERVINDO PIZZA')

    
class StylishPizza(Pizza):
    def add_ingrentients(self) -> Any:
        print(f'{self.__class__.__name__} - adicionando ingredientes: presunto, queijo e tomate')

    def cook(self) -> Any:
        print(f'{self.__class__.__name__} - cozinhando por 45min no forno a lenha')
    

class PizzaVegana(Pizza):
    def hook_before_add_ingrentients(self):
        print(f'{self.__class__.__name__} - lavando os ingredientes')
    def add_ingrentients(self) -> Any:
        print(f'{self.__class__.__name__} - adicionando ingredientes: salada, tomate e etc')

    def cook(self) -> Any:
        print(f'{self.__class__.__name__} - cozinhando por 5 min no forno comum')


if __name__ == '__main__':
    a_moda = StylishPizza()
    a_moda.prapare()

    print()

    veg_pizza = PizzaVegana()
    veg_pizza.prapare()
