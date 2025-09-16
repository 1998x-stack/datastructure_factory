from __future__ import annotations
import heapq
from typing import Dict, Tuple, Hashable, Iterable
from ..factory.registry import register_algo

@register_algo("dijkstra")
def dijkstra(adj_w: Dict[Hashable, Dict[Hashable, float]], src: Hashable) -> Tuple[Dict[Hashable, float], Dict[Hashable, Hashable]]:
    """堆优化 Dijkstra。adj_w: {u: {v: w}}"""
    dist: Dict[Hashable, float] = {src: 0.0}
    prev: Dict[Hashable, Hashable] = {}
    pq: list[tuple[float, Hashable]] = [(0.0, src)]
    vis: set[Hashable] = set()

    while pq:
        d, u = heapq.heappop(pq)
        if u in vis: continue
        vis.add(u)
        for v, w in adj_w.get(u, {}).items():
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd; prev[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, prev
