from __future__ import annotations
from typing import Iterable, Hashable, List
from ..factory.registry import register_adt

@register_adt("bloom")
class BloomFilter:
    """布隆过滤器（简单位图版）。"""
    def __init__(self, m_bits: int = 1<<20, k_hashes: int = 7, seeds: Iterable[int] | None = None):
        assert m_bits > 0 and k_hashes > 0
        self.m = m_bits
        self.k = k_hashes
        self.bits = bytearray((m_bits + 7) // 8)
        if seeds is None:
            self.seeds = [146959810, 2166136261, 2654435761, 40503, 1315423911, 374761393, 86028157][:self.k]
        else:
            ss = list(seeds)
            assert len(ss) >= self.k
            self.seeds = ss[:self.k]

    def __len__(self) -> int: return self.m
    def clear(self) -> None: self.bits = bytearray(len(self.bits))
    def extend(self, items: Iterable[Hashable]) -> None:
        for x in items: self.add(x)

    def _hashes(self, x: Hashable) -> List[int]:
        h = hash(x)
        return [((h ^ s) * 11400714819323198485 & 0xFFFFFFFFFFFFFFFF) % self.m for s in self.seeds]

    def _setbit(self, i: int) -> None:
        self.bits[i >> 3] |= (1 << (i & 7))
    def _getbit(self, i: int) -> bool:
        return (self.bits[i >> 3] >> (i & 7)) & 1 == 1

    def add(self, x: Hashable) -> None:
        for i in self._hashes(x): self._setbit(int(i))

    def contains(self, x: Hashable) -> bool:
        return all(self._getbit(int(i)) for i in self._hashes(x))
