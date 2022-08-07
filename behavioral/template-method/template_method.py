from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation_1()
        self.operation_2()
        self.class_base_method()

    def hook(self): pass

    def class_base_method(self):
        print('Olá eu sou da classe abstratra e serei executada')

    @abstractmethod
    def operation_1(self): pass

    @abstractmethod
    def operation_2(self): pass



class ConcreteClass1(Abstract):
    def hook(self):
        print('eu vou execultar o hook')

    def operation_1(self):
        print('Operação 1 concluida')

    def operation_2(self):
        print('Operação 2 concluida')


class ConcreteClass2(Abstract):
    def operation_1(self):
        print('Operação 1 concluida ( de maneira diferente )')

    def operation_2(self):
        print('Operação 2 concluida ( de maneira diferente )')


if __name__ == '__main__':
    c1 = ConcreteClass1()
    c1.template_method()

    print()

    c2 = ConcreteClass2()
    c2.template_method()