from __future__ import annotations
from typing import Dict, List
from pathlib import Path
import matplotlib
matplotlib.use("Agg")  # 无显示环境下也能渲染
import matplotlib.pyplot as plt

def plot_curves(results: Dict[str, List[float]], sizes: List[int], title: str, filename: str) -> str:
    """绘制多算法曲线并保存到 data/reports/filename，返回文件路径。"""
    outdir = Path("data/reports"); outdir.mkdir(parents=True, exist_ok=True)
    fig = plt.figure(figsize=(8, 5))
    for name, ys in results.items():
        plt.plot(sizes, ys, marker="o", label=name)
    plt.xlabel("Input size (n)")
    plt.ylabel("Time (s)")
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    outpath = outdir / filename
    fig.tight_layout()
    fig.savefig(outpath)
    plt.close(fig)
    return str(outpath)
