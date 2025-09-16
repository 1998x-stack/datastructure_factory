from __future__ import annotations
from typing import Dict, List, Hashable, Iterable
from ..factory.registry import register_adt

@register_adt("graph")
class Graph:
    """邻接表表示无向/有向图。"""
    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adj: Dict[Hashable, List[Hashable]] = {}

    def add_edge(self, u: Hashable, v: Hashable) -> None:
        self.adj.setdefault(u, []).append(v)
        if not self.directed:
            self.adj.setdefault(v, []).append(u)

    def vertices(self) -> Iterable[Hashable]:
        return self.adj.keys()

    def neighbors(self, u: Hashable) -> Iterable[Hashable]:
        return self.adj.get(u, [])
