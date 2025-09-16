from __future__ import annotations
from typing import Optional, Generic, TypeVar
from ..factory.registry import register_adt

T = TypeVar("T")

class _N(Generic[T]):
    __slots__ = ("k","l","r","h")
    def __init__(self, k: T):
        self.k = k; self.l: Optional["_N[T]"] = None; self.r: Optional["_N[T]"] = None; self.h = 1

def _h(n: Optional[_N[T]]) -> int: return n.h if n else 0
def _upd(n: _N[T]) -> None: n.h = max(_h(n.l), _h(n.r)) + 1
def _bf(n: _N[T]) -> int: return _h(n.l) - _h(n.r)

def _rot_r(y: _N[T]) -> _N[T]:
    x = y.l; assert x
    T2 = x.r
    x.r = y; y.l = T2
    _upd(y); _upd(x); return x

def _rot_l(x: _N[T]) -> _N[T]:
    y = x.r; assert y
    T2 = y.l
    y.l = x; x.r = T2
    _upd(x); _upd(y); return y

def _balance(n: _N[T]) -> _N[T]:
    _upd(n)
    b = _bf(n)
    if b > 1:
        if _bf(n.l) < 0: n.l = _rot_l(n.l)  # type: ignore
        return _rot_r(n)
    if b < -1:
        if _bf(n.r) > 0: n.r = _rot_r(n.r)  # type: ignore
        return _rot_l(n)
    return n

@register_adt("avl")
class AVL(Generic[T]):
    def __init__(self):
        self.root: Optional[_N[T]] = None

    def insert(self, k: T) -> None:
        def _ins(n: Optional[_N[T]], k: T) -> _N[T]:
            if not n: return _N(k)
            if k < n.k: n.l = _ins(n.l, k)
            elif k > n.k: n.r = _ins(n.r, k)
            else: return n
            return _balance(n)
        self.root = _ins(self.root, k)

    def _min(self, n: _N[T]) -> _N[T]:
        while n.l: n = n.l
        return n

    def delete(self, k: T) -> None:
        def _del(n: Optional[_N[T]], k: T) -> Optional[_N[T]]:
            if not n: return None
            if k < n.k: n.l = _del(n.l, k)
            elif k > n.k: n.r = _del(n.r, k)
            else:
                if not n.l: return n.r
                if not n.r: return n.l
                s = self._min(n.r)
                n.k = s.k
                n.r = _del(n.r, s.k)
            return _balance(n) if n else None
        self.root = _del(self.root, k)
