from __future__ import annotations
from typing import Generic, TypeVar, Iterable, Optional
from ..factory.registry import register_adt
from ..core.adt_base import ADTBase

T = TypeVar("T")

@register_adt("stack")
class Stack(ADTBase[T]):
    def __init__(self, data: Optional[Iterable[T]] = None):
        self._buf: list[T] = []
        if data: self.extend(data)
    def __len__(self) -> int: return len(self._buf)
    def clear(self) -> None: self._buf.clear()
    def extend(self, items: Iterable[T]) -> None:
        self._buf.extend(items)
    def push(self, x: T) -> None: self._buf.append(x)
    def pop(self) -> T: return self._buf.pop()
    def peek(self) -> T: return self._buf[-1]

@register_adt("queue")
class Queue(ADTBase[T]):
    """数组 + 头指针实现的队列，避免 O(n) 的 pop(0)。"""
    def __init__(self, data: Optional[Iterable[T]] = None):
        self._buf: list[T] = []
        self._head = 0
        if data: self.extend(data)
    def __len__(self) -> int: return len(self._buf) - self._head
    def clear(self) -> None:
        self._buf.clear(); self._head = 0
    def extend(self, items: Iterable[T]) -> None:
        self._buf.extend(items)
    def push(self, x: T) -> None: self._buf.append(x)
    def pop(self) -> T:
        if self._head >= len(self._buf): raise IndexError("pop from empty")
        x = self._buf[self._head]; self._head += 1
        # 定期压缩空间
        if self._head > 32 and self._head * 2 > len(self._buf):
            self._buf = self._buf[self._head:]; self._head = 0
        return x
