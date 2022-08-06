from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List, Tuple


class Light:
    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self) -> None:
        print(f'Light {self.name} in {self.room_name} is now ON')

    def off(self) -> None:
        print(f'Light {self.name} in {self.room_name} is now OFF')

    def change_color(self, color: str) -> None:
        self.color = color
        print(f'Light {self.name} in {self.room_name} is now {self.color}')


class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass 


class LigthOnCommand(ICommand):
    def __init__(self, ligth: Light) -> None:
        self.ligth = ligth

    def execute(self) -> None:
        self.ligth.on()

    def undo(self) -> None:
        self.ligth.off()


class LigthChangeColor(ICommand):
    def __init__(self, ligth: Light, color: str) -> None:
        self.ligth = ligth
        self.color = color
        self._old_color = self.ligth.color

    def execute(self) -> None:
        self._old_color = self.ligth.color
        self.ligth.change_color(self.color)

    def undo(self) -> None:
        self.ligth.change_color(self._old_color)

class RemoteController:
    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}
        self._undos: List[Tuple[str, str]] = []

    def button_add_command(self, button_name: str, command: ICommand) -> None:
        self._buttons[button_name] = command

    def button_pressed(self, button: str) -> None:
        if button in self._buttons:
            self._buttons[button].execute()
            self._undos.append((button, 'execute'))

    def button_pressed_again(self, button: str) -> None:
        if button in self._buttons:
            self._buttons[button].undo()
            self._undos.append((button, 'undo'))

    def global_undo(self):
        if not self._undos:
            print('Nothing to undo')
            return None
        
        button_name, action = self._undos[-1]

        if action == 'execute':
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()

        self._undos.pop()

if __name__ == '__main__':
    bedroom_ligth = Light('led lamp', 'bedroom')

    bedroom_ligth_on = LigthOnCommand(bedroom_ligth)

    bedroom_ligth_blue = LigthChangeColor(bedroom_ligth, 'blue')
    bedroom_ligth_red = LigthChangeColor(bedroom_ligth, 'red')

    remote = RemoteController()
    remote.button_add_command('first button', bedroom_ligth_on)
    remote.button_add_command('second button', bedroom_ligth_blue)
    remote.button_add_command('trird button', bedroom_ligth_red)

    remote.button_pressed('first button')
    remote.button_pressed('second button')
    remote.button_pressed('trird button')
    remote.button_pressed_again('trird button')

    print()

    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
