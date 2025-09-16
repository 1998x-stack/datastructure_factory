from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable, Generic, TypeVar

T = TypeVar("T")

class ADTBase(ABC, Generic[T]):
    """ADT 抽象基类，统一接口风格。"""

    @abstractmethod
    def __len__(self) -> int: ...

    @abstractmethod
    def clear(self) -> None: ...

    @abstractmethod
    def extend(self, items: Iterable[T]) -> None: ...
