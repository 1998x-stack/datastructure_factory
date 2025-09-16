from __future__ import annotations
import random
from typing import Optional, Generic, TypeVar
from ..factory.registry import register_adt

T = TypeVar("T")

class _N(Generic[T]):
    __slots__ = ("key","prio","l","r")
    def __init__(self, key: T, prio: int):
        self.key = key; self.prio = prio
        self.l: Optional["_N[T]"] = None
        self.r: Optional["_N[T]"] = None

def _rot_r(y: _N[T]) -> _N[T]:
    x = y.l; assert x
    y.l = x.r; x.r = y; return x

def _rot_l(x: _N[T]) -> _N[T]:
    y = x.r; assert y
    x.r = y.l; y.l = x; return y

@register_adt("treap")
class Treap(Generic[T]):
    """Treap（树堆）：按 key BST、按 prio 堆。"""
    def __init__(self, seed: int = 42):
        self.root: Optional[_N[T]] = None
        self.rng = random.Random(seed)

    def _ins(self, n: Optional[_N[T]], k: T) -> _N[T]:
        if not n: return _N(k, self.rng.randint(1, 10**9))
        if k < n.key:
            n.l = self._ins(n.l, k)
            if n.l and n.l.prio < n.prio: n = _rot_r(n)
        elif k > n.key:
            n.r = self._ins(n.r, k)
            if n.r and n.r.prio < n.prio: n = _rot_l(n)
        return n

    def insert(self, k: T) -> None:
        self.root = self._ins(self.root, k)

    def _del(self, n: Optional[_N[T]], k: T) -> Optional[_N[T]]:
        if not n: return None
        if k < n.key: n.l = self._del(n.l, k)
        elif k > n.key: n.r = self._del(n.r, k)
        else:
            if not n.l: return n.r
            if not n.r: return n.l
            if n.l.prio < n.r.prio:
                n = _rot_r(n); n.r = self._del(n.r, k)
            else:
                n = _rot_l(n); n.l = self._del(n.l, k)
        return n

    def delete(self, k: T) -> None:
        self.root = self._del(self.root, k)

    def search(self, k: T) -> bool:
        cur = self.root
        while cur:
            if k == cur.key: return True
            cur = cur.l if k < cur.key else cur.r
        return False
