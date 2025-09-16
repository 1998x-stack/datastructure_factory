from __future__ import annotations
from typing import Generic, TypeVar, Optional, Iterable
from ..factory.registry import register_adt
from ..core.adt_base import ADTBase

T = TypeVar("T")

class _Node(Generic[T]):
    __slots__ = ("val", "next", "prev")
    def __init__(self, val: T):
        self.val = val
        self.next: Optional["_Node[T]"] = None
        self.prev: Optional["_Node[T]"] = None

@register_adt("singly_linked_list")
class SinglyLinkedList(ADTBase[T]):
    def __init__(self, data: Optional[Iterable[T]] = None):
        self.head: Optional[_Node[T]] = None
        self._n = 0
        if data:
            self.extend(data)

    def __len__(self) -> int: return self._n
    def clear(self) -> None:
        self.head = None
        self._n = 0

    def extend(self, items: Iterable[T]) -> None:
        for x in items:
            self.append(x)

    def append(self, x: T) -> None:
        node = _Node(x)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self._n += 1

    def delete_value(self, x: T) -> bool:
        prev = None
        cur = self.head
        while cur:
            if cur.val == x:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                self._n -= 1
                return True
            prev, cur = cur, cur.next
        return False

@register_adt("deque_list")
class DequeList(ADTBase[T]):
    """双向链表实现的双端队列。"""
    def __init__(self, data: Optional[Iterable[T]] = None):
        self.head: Optional[_Node[T]] = None
        self.tail: Optional[_Node[T]] = None
        self._n = 0
        if data:
            self.extend(data)

    def __len__(self) -> int: return self._n
    def clear(self) -> None:
        self.head = self.tail = None
        self._n = 0

    def extend(self, items: Iterable[T]) -> None:
        for x in items:
            self.push_back(x)

    def push_front(self, x: T) -> None:
        node = _Node(x)
        node.next = self.head
        if self.head:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node
        self._n += 1

    def push_back(self, x: T) -> None:
        node = _Node(x)
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self._n += 1

    def pop_front(self) -> T:
        if not self.head: raise IndexError("pop_front from empty")
        node = self.head
        self.head = node.next
        if self.head: self.head.prev = None
        else: self.tail = None
        self._n -= 1
        return node.val

    def pop_back(self) -> T:
        if not self.tail: raise IndexError("pop_back from empty")
        node = self.tail
        self.tail = node.prev
        if self.tail: self.tail.next = None
        else: self.head = None
        self._n -= 1
        return node.val
