from __future__ import annotations
from typing import Generic, TypeVar, Optional, Dict
from ..factory.registry import register_adt

K = TypeVar("K")
V = TypeVar("V")

class _Node(Generic[K, V]):
    __slots__ = ("k", "v", "prev", "next")
    def __init__(self, k: K, v: V):
        self.k, self.v = k, v
        self.prev: Optional["_Node[K, V]"] = None
        self.next: Optional["_Node[K, V]"] = None

@register_adt("lru_cache")
class LRUCache(Generic[K, V]):
    """LRU: 哈希表 + 双向链表，get/put O(1)。"""

    def __init__(self, capacity: int = 128):
        self.cap = capacity
        self.map: Dict[K, _Node[K, V]] = {}
        # 伪头尾哨兵
        self.head = _Node(None, None)  # type: ignore
        self.tail = _Node(None, None)  # type: ignore
        self.head.next = self.tail; self.tail.prev = self.head

    def _remove(self, node: _Node[K, V]) -> None:
        p, n = node.prev, node.next
        assert p and n
        p.next = n; n.prev = p

    def _append_front(self, node: _Node[K, V]) -> None:
        n1 = self.head.next
        assert n1
        node.prev = self.head; node.next = n1
        self.head.next = node; n1.prev = node

    def get(self, k: K) -> Optional[V]:
        node = self.map.get(k)
        if not node: return None
        self._remove(node); self._append_front(node)
        return node.v

    def put(self, k: K, v: V) -> None:
        node = self.map.get(k)
        if node:
            node.v = v
            self._remove(node); self._append_front(node)
            return
        node = _Node(k, v)
        self.map[k] = node
        self._append_front(node)
        if len(self.map) > self.cap:
            # 淘汰尾部
            last = self.tail.prev
            assert last and last is not self.head
            self._remove(last)
            self.map.pop(last.k, None)
