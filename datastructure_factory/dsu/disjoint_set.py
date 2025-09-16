from __future__ import annotations
from typing import Dict, Hashable
from ..factory.registry import register_adt

@register_adt("dsu")
class DisjointSet:
    """并查集（路径压缩 + 按秩合并），近似 O(α(n))。"""
    def __init__(self):
        self.parent: Dict[Hashable, Hashable] = {}
        self.rank: Dict[Hashable, int] = {}

    def find(self, x: Hashable) -> Hashable:
        if x not in self.parent:
            self.parent[x] = x; self.rank[x] = 0
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: Hashable, y: Hashable) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx == ry: return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
