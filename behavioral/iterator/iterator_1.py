from collections.abc import Iterator, Iterable
from typing import Any, List

class MyIterator(Iterator):
    def __init__(self, colecction: List[Any]) -> None:
        self._colecction = colecction
        self._index = 0

    def __next__(self) -> Any:
        try:
            item = self._colecction[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class ReverseIterator(Iterator):
    def __init__(self, colecction: List[Any]) -> None:
        self._colecction = colecction
        self._index = -1

    def __next__(self) -> Any:
        try:
            item = self._colecction[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self) -> None:
        self._items: List[Any] = []
        self._my_iterator = MyIterator(self._items)

    def add(self, items: Any) -> None:
        self._items.append(items)

    def __iter__(self) -> Iterator:
        return self._my_iterator

    def reverse_iterator(self) -> Iterator:
        return ReverseIterator(self._items)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'


if __name__ == '__main__':
    mylist = MyList()

    mylist.add('Luiz')
    mylist.add('José')
    mylist.add('Aninha')

    print(mylist)
    print()

    print('Roubei', next(iter(mylist)))
    print()

    for value in mylist:
        print(value)

    print()

    for value in mylist.reverse_iterator():
        print(value)