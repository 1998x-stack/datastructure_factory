from __future__ import annotations
from typing import Any, Optional, List, Tuple, Callable
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def _get_children(node: Any) -> Tuple[Optional[Any], Optional[Any]]:
    # 兼容不同节点字段：BST(key,left,right)；AVL(k,l,r)；RBT(key,left,right,color)；Treap(key,l,r)
    if node is None: return None, None
    if hasattr(node, "left") or hasattr(node, "right"):
        return getattr(node, "left", None), getattr(node, "right", None)
    return getattr(node, "l", None), getattr(node, "r", None)

def _get_key(node: Any) -> Any:
    return getattr(node, "key", getattr(node, "k", None))

def _get_color(node: Any) -> str:
    # 红黑：node.color == 0 红；其它树统一蓝色
    if hasattr(node, "color"):
        return "tab:red" if getattr(node, "color") == 0 else "k"
    return "tab:blue"

def _layout(root: Any) -> dict[Any, Tuple[float, float]]:
    # 中序编号 -> x，深度 -> y
    x = 0
    pos: dict[Any, Tuple[float, float]] = {}
    def dfs(n: Any, d: int):
        nonlocal x
        if not n: return
        l, r = _get_children(n)
        dfs(l, d+1)
        pos[n] = (x, -d)
        x += 1
        dfs(r, d+1)
    dfs(root, 0)
    # scale
    return {n: (px, py) for n,(px,py) in pos.items()}

def _edges(root: Any) -> List[Tuple[Any, Any]]:
    es: List[Tuple[Any, Any]] = []
    def go(n: Any):
        if not n: return
        l, r = _get_children(n)
        if l: es.append((n, l)); go(l)
        if r: es.append((n, r)); go(r)
    go(root); return es

def draw_tree(root: Any, title: str, outpath: str) -> str:
    Path(outpath).parent.mkdir(parents=True, exist_ok=True)
    pos = _layout(root)
    es = _edges(root)
    fig = plt.figure(figsize=(8, 4.5))
    ax = plt.gca(); ax.axis("off")
    for u,v in es:
        x1,y1 = pos[u]; x2,y2 = pos[v]
        ax.plot([x1,x2],[y1,y2], color="0.6")
    for n,(x,y) in pos.items():
        ax.scatter([x],[y], s=600, facecolors="white", edgecolors=_get_color(n), linewidths=2)
        ax.text(x, y, str(_get_key(n)), ha="center", va="center")
    ax.set_title(title)
    fig.tight_layout(); fig.savefig(outpath); plt.close(fig)
    return outpath

def viz_insert_evolution(make_tree: Callable[[], Any], inserts: List[int], outdir: str, name: str) -> List[str]:
    frames: List[str] = []
    t = make_tree()
    for step, k in enumerate(inserts, start=1):
        # 支持不同树的 insert 接口
        if hasattr(t, "insert"): t.insert(k)
        elif hasattr(t, "put"): t.put(k)
        else: raise RuntimeError("Tree insert interface not found.")
        path = Path(outdir) / f"{name}_step_{step:03d}.png"
        root = getattr(t, "root", None)
        frames.append(draw_tree(root, f"{name}: insert {k}", str(path)))
    return frames
