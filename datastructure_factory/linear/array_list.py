from __future__ import annotations
from typing import Generic, TypeVar, Iterable, Optional
from loguru import logger
from ..factory.registry import register_adt
from ..core.adt_base import ADTBase

T = TypeVar("T")

@register_adt("array_list")
class DynamicArray(ADTBase[T], Generic[T]):
    """动态数组：支持容量扩张，摊还 O(1) push/pop。

    Args:
        init_capacity: 初始容量
        data: 初始数据
    """

    def __init__(self, init_capacity: int = 8, data: Optional[Iterable[T]] = None):
        self._n = 0
        self._cap = max(1, init_capacity)
        self._buf = [None] * self._cap  # type: ignore
        logger.debug(f"DynamicArray init cap={self._cap}")
        if data:
            self.extend(data)

    def __len__(self) -> int:
        return self._n

    def _resize(self, new_cap: int) -> None:
        logger.debug(f"Resize from {self._cap} -> {new_cap}")
        tmp = [None] * new_cap  # type: ignore
        for i in range(self._n):
            tmp[i] = self._buf[i]
        self._buf = tmp
        self._cap = new_cap

    def append(self, x: T) -> None:
        if self._n >= self._cap:
            self._resize(self._cap * 2)
        self._buf[self._n] = x
        self._n += 1

    def pop(self) -> T:
        if self._n == 0:
            raise IndexError("pop from empty array")
        self._n -= 1
        x = self._buf[self._n]
        self._buf[self._n] = None
        if 0 < self._n <= self._cap // 4:
            self._resize(max(1, self._cap // 2))
        return x  # type: ignore

    def __getitem__(self, i: int) -> T:
        if not 0 <= i < self._n:
            raise IndexError("index out of range")
        return self._buf[i]  # type: ignore

    def __setitem__(self, i: int, v: T) -> None:
        if not 0 <= i < self._n:
            raise IndexError("index out of range")
        self._buf[i] = v

    def insert(self, i: int, v: T) -> None:
        if not 0 <= i <= self._n:
            raise IndexError("index out of range")
        if self._n >= self._cap:
            self._resize(self._cap * 2)
        for j in range(self._n, i, -1):
            self._buf[j] = self._buf[j-1]
        self._buf[i] = v
        self._n += 1

    def delete(self, i: int) -> T:
        if not 0 <= i < self._n:
            raise IndexError("index out of range")
        v = self._buf[i]
        for j in range(i, self._n - 1):
            self._buf[j] = self._buf[j+1]
        self._n -= 1
        self._buf[self._n] = None
        if 0 < self._n <= self._cap // 4:
            self._resize(max(1, self._cap // 2))
        return v  # type: ignore

    def clear(self) -> None:
        self._n = 0
        self._buf = [None] * max(1, self._cap)

    def extend(self, items: Iterable[T]) -> None:
        for x in items:
            self.append(x)
