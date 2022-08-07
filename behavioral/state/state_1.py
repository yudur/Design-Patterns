from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        print('Tentando execultar pending()')
        self.state.pending()
        print('Estado atual:', self.state)
        print()

    def approve(self) -> None:
        print('Tentando execultar approve()') 
        self.state.approve()
        print('Estado atual:', self.state)
        print()


    def reject(self) -> None:
        print('Tentando execultar reject()') 
        self.state.reject()
        print('Estado atual:', self.state)
        print()


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def approve(self) -> None: pass

    @abstractmethod
    def reject(self) -> None: pass

    def __str__(self) -> str:
        return self.__class__.__name__


class PaymentPending(OrderState):
    def pending(self) -> None:
        print('Pagamento já pendente, não posso faser nada.')

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('Pagamento aprovado')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagmamento rejeitado')


class PaymentApproved(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('Pagmamento pendente')

    def approve(self) -> None:
        print('Pagamento já aprovado, não posso faser nada.')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('Pagmamento recusado')


class PaymentRejected(OrderState):
    def pending(self) -> None:
        print('Pagmamento recusado. Não vou mover para pendente.')

    def approve(self) -> None:
        print('Pagmamento recusado. Não vou mover para aprovado.')

    def reject(self) -> None:
        print('Pagmamento recusado. Não vou recusar novamente.')


if __name__ == '__main__':
    order = Order()

    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.reject()
    order.pending()
