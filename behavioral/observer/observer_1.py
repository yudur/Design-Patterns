
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List


class IObsevable(ABC):
    @property
    @abstractmethod
    def state(self): pass
    
    @abstractmethod
    def add_observer(self, observer: IObsever) -> None: pass

    @abstractmethod
    def remove_observer(self, observer: IObsever) -> None: pass

    @abstractmethod
    def notefy_observers(self) -> None: pass
        

class WeatherStation(IObsevable):
    def __init__(self) -> None:
        self._obeservers: List[IObsever] = []
        self._state: Dict = {}

    @property
    def state(self):
       return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notefy_observers()

    def reset_state(self):
        self._state = {}
        self.notefy_observers()

    def add_observer(self, observer: IObsever) -> None:
        self._obeservers.append(observer)

    def remove_observer(self, observer: IObsever) -> None:
        if observer in self._obeservers:
            self._obeservers.remove(observer)

    def notefy_observers(self) -> None:
        for observer in self._obeservers:
            observer.update()
        print()


class IObsever(ABC):
    @abstractmethod
    def update(self) -> None: pass


class SmartPhone(IObsever):
    def __init__(self, name: str, observable: IObsevable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} o objeto {observable_name} acabou de ser atualizado => {self.observable.state}')

class Notebook(IObsever):
    def __init__(self, name: str, observable: IObsevable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'sou o notebook e irei fazer outra coisa com os dados')


if __name__ == '__main__':
    weather_station = WeatherStation()
    
    smartphone1 = SmartPhone('Xiomi A3', weather_station)
    smartphone2 = SmartPhone('IPhone', weather_station)

    weather_station.add_observer(smartphone1)
    weather_station.add_observer(smartphone2)

    weather_station.state = {'temperature': '31'}
    weather_station.state = {'humidity': '87'}

    weather_station.remove_observer(smartphone2)
    weather_station.reset_state()