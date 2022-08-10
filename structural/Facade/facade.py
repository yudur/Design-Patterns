
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
        print(f'{self.name} o objeto {observable_name}'\
              f'acabou de ser atualizado => {self.observable.state}')

class Notebook(IObsever):
    def __init__(self, name: str, observable: IObsevable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'sou o notebook e irei fazer outra coisa com os dados')


class WeatherStationFacade:
    def __init__(self) -> None:
        self.weather_station = WeatherStation()
        
        self.smartphone1 = SmartPhone('Xiomi A3', self.weather_station)
        self.smartphone2 = SmartPhone('IPhone', self.weather_station)

        self.weather_station.add_observer(self.smartphone1)
        self.weather_station.add_observer(self.smartphone2)

    def add_observer(self, observer: IObsever) -> None:
        self.weather_station.add_observer()

    def ChangeState(self, state: Dict) -> None:
        self.weather_station.state = state

    def remove_observer(self, observer: IObsever):
        self.weather_station.remove_observer(observer)

    def reset_state(self):
        self.weather_station.reset_state()


if __name__ == '__main__':
    weather_station = WeatherStationFacade()

    weather_station.ChangeState({'temperature': '31'})
    weather_station.ChangeState({'humidity': '87'})

    weather_station.reset_state()
