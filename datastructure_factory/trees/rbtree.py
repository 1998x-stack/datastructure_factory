from __future__ import annotations
from typing import Optional, Generic, TypeVar
from ..factory.registry import register_adt

T = TypeVar("T")
RED, BLACK = 0, 1

class _N(Generic[T]):
    __slots__ = ("key","left","right","parent","color")
    def __init__(self, key: T, color: int = RED):
        self.key = key
        self.left: Optional["_N[T]"] = None
        self.right: Optional["_N[T]"] = None
        self.parent: Optional["_N[T]"] = None
        self.color = color

def _is_red(n: Optional[_N[T]]) -> bool: return bool(n and n.color == RED)

@register_adt("rbtree")
class RBTree(Generic[T]):
    """红黑树（CLRS 风格，支持插入与删除）。"""
    def __init__(self):
        self.root: Optional[_N[T]] = None

    # 旋转
    def _rot_l(self, x: _N[T]) -> None:
        y = x.right; assert y
        x.right = y.left
        if y.left: y.left.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x is x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left = x; x.parent = y

    def _rot_r(self, y: _N[T]) -> None:
        x = y.left; assert x
        y.left = x.right
        if x.right: x.right.parent = y
        x.parent = y.parent
        if not y.parent: self.root = x
        elif y is y.parent.left: y.parent.left = x
        else: y.parent.right = x
        x.right = y; y.parent = x

    # 插入
    def insert(self, key: T) -> None:
        z = _N(key, RED)
        y: Optional[_N[T]] = None
        x = self.root
        while x:
            y = x
            x = x.left if z.key < x.key else x.right
        z.parent = y
        if not y: self.root = z
        elif z.key < y.key: y.left = z
        else: y.right = z
        self._insert_fix(z)

    def _insert_fix(self, z: _N[T]) -> None:
        while z.parent and _is_red(z.parent):
            if z.parent is z.parent.parent.left:  # type: ignore
                y = z.parent.parent.right  # 叔
                if _is_red(y):
                    z.parent.color = BLACK; y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z is z.parent.right:
                        z = z.parent
                        self._rot_l(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._rot_r(z.parent.parent)
            else:
                y = z.parent.parent.left
                if _is_red(y):
                    z.parent.color = BLACK; y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self._rot_r(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._rot_l(z.parent.parent)
        if self.root: self.root.color = BLACK

    # 删除
    def _transplant(self, u: _N[T], v: Optional[_N[T]]) -> None:
        if not u.parent: self.root = v
        elif u is u.parent.left: u.parent.left = v
        else: u.parent.right = v
        if v: v.parent = u.parent

    def _min(self, n: _N[T]) -> _N[T]:
        while n.left: n = n.left
        return n

    def delete(self, key: T) -> None:
        z = self._search_node(key)
        if not z: return
        y = z; y_orig_color = y.color
        if not z.left:
            x = z.right
            self._transplant(z, z.right)
        elif not z.right:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._min(z.right)
            y_orig_color = y.color
            x = y.right
            if y.parent is z:
                if x: x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right; y.right.parent = y  # type: ignore
            self._transplant(z, y)
            y.left = z.left; y.left.parent = y  # type: ignore
            y.color = z.color
        if y_orig_color == BLACK:
            self._delete_fix(x, parent=(y.parent if y else None))

    def _delete_fix(self, x: Optional[_N[T]], parent: Optional[_N[T]]) -> None:
        while (x is not self.root) and (not _is_red(x)):
            if x is (parent.left if parent else None):
                w = parent.right if parent else None
                if _is_red(w):
                    w.color = BLACK; parent.color = RED
                    self._rot_l(parent); w = parent.right
                if (not _is_red(w.left if w else None)) and (not _is_red(w.right if w else None)):
                    if w: w.color = RED
                    x = parent; parent = x.parent if x else None
                else:
                    if not _is_red(w.right if w else None):
                        if w and w.left: w.left.color = BLACK
                        if w: w.color = RED
                        if parent: self._rot_r(w)  # type: ignore
                        w = parent.right if parent else None
                    if w: w.color = parent.color if parent else BLACK
                    if parent: parent.color = BLACK
                    if w and w.right: w.right.color = BLACK
                    if parent: self._rot_l(parent)
                    x = self.root; parent = None
            else:
                w = parent.left if parent else None
                if _is_red(w):
                    w.color = BLACK; parent.color = RED
                    self._rot_r(parent); w = parent.left
                if (not _is_red(w.left if w else None)) and (not _is_red(w.right if w else None)):
                    if w: w.color = RED
                    x = parent; parent = x.parent if x else None
                else:
                    if not _is_red(w.left if w else None):
                        if w and w.right: w.right.color = BLACK
                        if w: w.color = RED
                        if parent: self._rot_l(w)  # type: ignore
                        w = parent.left if parent else None
                    if w: w.color = parent.color if parent else BLACK
                    if parent: parent.color = BLACK
                    if w and w.left: w.left.color = BLACK
                    if parent: self._rot_r(parent)
                    x = self.root; parent = None
        if x: x.color = BLACK

    def _search_node(self, key: T) -> Optional[_N[T]]:
        cur = self.root
        while cur:
            if key == cur.key: return cur
            cur = cur.left if key < cur.key else cur.right
        return None

    def search(self, key: T) -> bool:
        return self._search_node(key) is not None
