from __future__ import annotations
from typing import List, Optional, Generic, TypeVar
from ..factory.registry import register_adt

T = TypeVar("T")

class _Node(Generic[T]):
    def __init__(self, t: int, leaf: bool):
        self.t = t
        self.leaf = leaf
        self.keys: List[T] = []
        self.child: List["_Node[T]"] = []

@register_adt("btree")
class BTree(Generic[T]):
    """B-Tree（最小度 t >= 2），支持 search / insert。"""
    def __init__(self, t: int = 3):
        assert t >= 2, "t >= 2"
        self.t = t
        self.root = _Node[T](t, True)

    def search(self, k: T, x: Optional[_Node[T]] = None) -> bool:
        if x is None: x = self.root
        i = 0
        while i < len(x.keys) and k > x.keys[i]: i += 1
        if i < len(x.keys) and k == x.keys[i]: return True
        if x.leaf: return False
        return self.search(k, x.child[i])

    def insert(self, k: T) -> None:
        r = self.root
        if len(r.keys) == 2*self.t - 1:
            s = _Node[T](self.t, False)
            self.root = s
            s.child.append(r)
            self._split_child(s, 0)
            self._insert_nonfull(s, k)
        else:
            self._insert_nonfull(r, k)

    def _split_child(self, x: _Node[T], i: int) -> None:
        t = self.t
        y = x.child[i]
        z = _Node[T](t, y.leaf)
        x.child.insert(i+1, z)
        x.keys.insert(i, y.keys[t-1])
        z.keys = y.keys[t:(2*t-1)]
        y.keys = y.keys[0:t-1]
        if not y.leaf:
            z.child = y.child[t:(2*t)]
            y.child = y.child[0:t]

    def _insert_nonfull(self, x: _Node[T], k: T) -> None:
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(k)
            i = len(x.keys) - 2
            while i >= 0 and x.keys[i] > k:
                x.keys[i+1] = x.keys[i]; i -= 1
            x.keys[i+1] = k
        else:
            while i >= 0 and k < x.keys[i]: i -= 1
            i += 1
            if len(x.child[i].keys) == 2*self.t - 1:
                self._split_child(x, i)
                if k > x.keys[i]: i += 1
            self._insert_nonfull(x.child[i], k)
