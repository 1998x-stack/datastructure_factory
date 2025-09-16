from __future__ import annotations
from typing import List, Tuple, Hashable
from ..factory.registry import register_algo
from ..dsu.disjoint_set import DisjointSet

@register_algo("kruskal")
def kruskal(n_vertices: int, edges: List[Tuple[float, Hashable, Hashable]]) -> Tuple[float, List[Tuple[float, Hashable, Hashable]]]:
    """Kruskal 最小生成树，edges: (w,u,v)"""
    dsu = DisjointSet()
    weight = 0.0
    mst: List[Tuple[float, Hashable, Hashable]] = []
    for w,u,v in sorted(edges):
        if dsu.find(u) != dsu.find(v):
            dsu.union(u,v)
            mst.append((w,u,v))
            weight += w
    return weight, mst
