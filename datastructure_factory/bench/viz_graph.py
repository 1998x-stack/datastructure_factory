from __future__ import annotations
from typing import Dict, List, Hashable, Tuple, Iterable, Set
from pathlib import Path
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def _circle_layout(nodes: List[Hashable]) -> Dict[Hashable, Tuple[float, float]]:
    n = len(nodes)
    return {u: (math.cos(2*math.pi*i/n), math.sin(2*math.pi*i/n)) for i, u in enumerate(nodes)}

def _draw_frame(pos, edges, color_map, step, outdir: Path, title: str):
    fig = plt.figure(figsize=(6,6))
    ax = plt.gca(); ax.axis("off")
    # edges
    for (u,v) in edges:
        x1,y1 = pos[u]; x2,y2 = pos[v]
        ax.plot([x1,x2],[y1,y2], alpha=0.3)
    # nodes
    for u,(x,y) in pos.items():
        c = color_map.get(u, "lightgray")
        ax.scatter([x],[y], s=600, edgecolors="k", zorder=3, c=c)
        ax.text(x, y, str(u), ha="center", va="center", fontsize=12, zorder=4)
    ax.set_title(title)
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / f"frame_{step:03d}.png"
    fig.tight_layout()
    fig.savefig(path); plt.close(fig)
    return str(path)

def viz_bfs(adj: Dict[Hashable, Iterable[Hashable]], src: Hashable, outdir: str) -> List[str]:
    nodes = sorted(set(adj.keys()) | {v for u in adj for v in adj[u]})
    pos = _circle_layout(nodes)
    edges = set()
    for u in adj:
        for v in adj[u]:
            edges.add(tuple(sorted((u,v))))
    frames = []
    color = {}
    q: List[Hashable] = [src]
    seen: Set[Hashable] = {src}
    step = 0
    frames.append(_draw_frame(pos, edges, color, step, Path(outdir), f"BFS start @ {src}"))
    while q:
        u = q.pop(0)
        color[u] = "tab:green"
        step += 1
        frames.append(_draw_frame(pos, edges, color, step, Path(outdir), f"BFS visit {u}"))
        for v in adj.get(u, []):
            if v not in seen:
                seen.add(v); q.append(v)
                color[v] = "tab:orange"
                step += 1
                frames.append(_draw_frame(pos, edges, color, step, Path(outdir), f"BFS discover {v}"))
    return frames

def viz_dfs(adj: Dict[Hashable, Iterable[Hashable]], src: Hashable, outdir: str) -> List[str]:
    nodes = sorted(set(adj.keys()) | {v for u in adj for v in adj[u]})
    pos = _circle_layout(nodes)
    edges = set()
    for u in adj:
        for v in adj[u]:
            edges.add(tuple(sorted((u,v))))
    frames = []
    color = {}
    seen: Set[Hashable] = set()
    step = 0
    stack: List[Tuple[Hashable, int]] = [(src, 0)]
    frames.append(_draw_frame(pos, edges, color, step, Path(outdir), f"DFS start @ {src}"))
    while stack:
        u, it = stack.pop()
        if u not in seen:
            seen.add(u); color[u] = "tab:blue"
            step += 1
            frames.append(_draw_frame(pos, edges, color, step, Path(outdir), f"DFS visit {u}"))
            nbrs = list(adj.get(u, []))
            for v in reversed(nbrs):
                if v not in seen:
                    color[v] = color.get(v, "tab:orange")
                    step += 1
                    frames.append(_draw_frame(pos, edges, color, step, Path(outdir), f"DFS push {v}"))
                    stack.append((v, 0))
    return frames

def viz_topo_kahn(adj: Dict[Hashable, Iterable[Hashable]], outdir: str) -> List[str]:
    indeg = {u: 0 for u in adj}
    for u in adj:
        for v in adj[u]:
            indeg[v] = indeg.get(v, 0) + 1
            if v not in adj: adj[v] = []
    nodes = list(adj.keys())
    pos = _circle_layout(nodes)
    edges = set()
    for u in adj:
        for v in adj[u]:
            edges.add((u, v))  # 有向就不排序

    frames = []
    q = [u for u in nodes if indeg.get(u, 0) == 0]
    taken = []
    color = {u: ("tab:orange" if indeg.get(u,0)==0 else "lightgray") for u in nodes}
    step = 0
    frames.append(_draw_frame(pos, edges, color, step, Path(outdir), "Topo sort: init zero-indegree"))
    while q:
        u = q.pop(0)
        taken.append(u); color[u] = "tab:green"
        step += 1
        frames.append(_draw_frame(pos, edges, color, step, Path(outdir), f"Take {u}"))
        for v in adj.get(u, []):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v); color[v] = "tab:orange"
                step += 1
                frames.append(_draw_frame(pos, edges, color, step, Path(outdir), f"Unlock {v}"))
    return frames
