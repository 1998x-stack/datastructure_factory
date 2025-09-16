from __future__ import annotations
from typing import Generic, TypeVar, Iterable, Optional, Iterator, Tuple
from ..factory.registry import register_adt
from ..core.adt_base import ADTBase

K = TypeVar("K")
V = TypeVar("V")

@register_adt("hash_map")
class HashMap(ADTBase[Tuple[K, V]], Generic[K, V]):
    """拉链法哈希表，支持自动扩容/缩容。"""

    def __init__(self, capacity: int = 8, load_factor: float = 0.75):
        self._n = 0
        self._cap = max(4, capacity)
        self._load = load_factor
        self._buckets: list[list[tuple[K, V]]] = [[] for _ in range(self._cap)]

    def __len__(self) -> int: return self._n
    def clear(self) -> None:
        self._n = 0
        self._buckets = [[] for _ in range(self._cap)]

    def extend(self, items: Iterable[tuple[K, V]]) -> None:
        for k, v in items: self.put(k, v)

    def _idx(self, key: K) -> int:
        return (hash(key) & 0x7FFFFFFF) % self._cap

    def _rehash(self, new_cap: int) -> None:
        old_items = [(k, v) for bucket in self._buckets for (k, v) in bucket]
        self._cap = max(4, new_cap)
        self._buckets = [[] for _ in range(self._cap)]
        self._n = 0
        for k, v in old_items:
            self.put(k, v)

    def put(self, key: K, val: V) -> None:
        i = self._idx(key)
        bucket = self._buckets[i]
        for idx, (k, _) in enumerate(bucket):
            if k == key:
                bucket[idx] = (key, val)
                return
        bucket.append((key, val))
        self._n += 1
        if self._n > self._cap * self._load:
            self._rehash(self._cap * 2)

    def get(self, key: K, default: Optional[V] = None) -> Optional[V]:
        i = self._idx(key)
        for k, v in self._buckets[i]:
            if k == key:
                return v
        return default

    def remove(self, key: K) -> bool:
        i = self._idx(key)
        bucket = self._buckets[i]
        for idx, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(idx)
                self._n -= 1
                if self._cap > 8 and self._n < self._cap * 0.25:
                    self._rehash(self._cap // 2)
                return True
        return False

    def items(self) -> Iterator[tuple[K, V]]:
        for bucket in self._buckets:
            for kv in bucket:
                yield kv
