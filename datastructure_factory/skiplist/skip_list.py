from __future__ import annotations
import random
from typing import Generic, TypeVar, Optional, List, Iterable
from ..factory.registry import register_adt

K = TypeVar("K")
V = TypeVar("V")

class _Node(Generic[K, V]):
    __slots__ = ("key", "val", "forw")
    def __init__(self, key: Optional[K], val: Optional[V], level: int):
        self.key = key
        self.val = val
        self.forw: List[Optional["_Node[K, V]"]] = [None]*(level+1)

@register_adt("skip_list")
class SkipList(Generic[K, V]):
    """跳表：期望 O(log n) 查找/插入/删除。"""
    def __init__(self, max_level: int = 16, p: float = 0.5):
        self.max_level = max_level
        self.p = p
        self.level = 0
        self.head = _Node[K, V](None, None, max_level)
        self._n = 0

    def __len__(self) -> int: return self._n
    def clear(self) -> None:
        self.level = 0
        self.head = _Node(None, None, self.max_level)
        self._n = 0
    def extend(self, items: Iterable[tuple[K, V]]) -> None:
        for k, v in items: self.insert(k, v)

    def _rand_level(self) -> int:
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def search(self, key: K) -> Optional[V]:
        cur = self.head
        for i in reversed(range(self.level+1)):
            while cur.forw[i] and cur.forw[i].key < key:
                cur = cur.forw[i]
        cur = cur.forw[0]
        return cur.val if cur and cur.key == key else None

    def insert(self, key: K, val: V) -> None:
        update = [None]*(self.max_level+1)
        cur = self.head
        for i in reversed(range(self.level+1)):
            while cur.forw[i] and cur.forw[i].key < key:
                cur = cur.forw[i]
            update[i] = cur
        cur = cur.forw[0]
        if cur and cur.key == key:
            cur.val = val
            return
        lvl = self._rand_level()
        if lvl > self.level:
            for i in range(self.level+1, lvl+1):
                update[i] = self.head
            self.level = lvl
        node = _Node(key, val, lvl)
        for i in range(lvl+1):
            node.forw[i] = update[i].forw[i]
            update[i].forw[i] = node
        self._n += 1

    def delete(self, key: K) -> bool:
        update = [None]*(self.max_level+1)
        cur = self.head
        for i in reversed(range(self.level+1)):
            while cur.forw[i] and cur.forw[i].key < key:
                cur = cur.forw[i]
            update[i] = cur
        cur = cur.forw[0]
        if not cur or cur.key != key:
            return False
        for i in range(self.level+1):
            if update[i].forw[i] != cur: break
            update[i].forw[i] = cur.forw[i]
        while self.level > 0 and self.head.forw[self.level] is None:
            self.level -= 1
        self._n -= 1
        return True
