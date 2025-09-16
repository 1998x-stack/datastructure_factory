from __future__ import annotations
from typing import Generic, TypeVar, Iterable, Callable, Optional
from ..factory.registry import register_adt

T = TypeVar("T")

@register_adt("min_heap")
class MinHeap(Generic[T]):
    """二叉最小堆，使用数组实现。"""
    def __init__(self, data: Optional[Iterable[T]] = None, key: Callable[[T], T] | None = None):
        self.a: list[T] = []
        self.key = key or (lambda x: x)
        if data:
            self.a = list(data)
            for i in reversed(range(len(self.a)//2)):
                self._down(i)

    def __len__(self) -> int: return len(self.a)
    def clear(self) -> None: self.a.clear()
    def extend(self, items: Iterable[T]) -> None:
        for x in items: self.push(x)

    def _less(self, i: int, j: int) -> bool:
        return self.key(self.a[i]) < self.key(self.a[j])

    def _swap(self, i: int, j: int) -> None:
        self.a[i], self.a[j] = self.a[j], self.a[i]

    def _up(self, i: int) -> None:
        while i > 0:
            p = (i - 1) // 2
            if self._less(i, p):
                self._swap(i, p); i = p
            else: break

    def _down(self, i: int) -> None:
        n = len(self.a)
        while True:
            l, r = 2*i+1, 2*i+2
            m = i
            if l < n and self._less(l, m): m = l
            if r < n and self._less(r, m): m = r
            if m == i: break
            self._swap(i, m); i = m

    def push(self, x: T) -> None:
        self.a.append(x); self._up(len(self.a)-1)

    def pop(self) -> T:
        if not self.a: raise IndexError("pop from empty heap")
        self._swap(0, len(self.a)-1)
        x = self.a.pop()
        if self.a: self._down(0)
        return x

    def peek(self) -> T:
        if not self.a: raise IndexError("peek from empty heap")
        return self.a[0]
