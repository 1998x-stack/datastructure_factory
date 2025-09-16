from __future__ import annotations
from typing import List
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def _lps(pat: str) -> List[int]:
    lps = [0]*len(pat); j = 0
    for i in range(1, len(pat)):
        while j and pat[i] != pat[j]: j = lps[j-1]
        if pat[i] == pat[j]: j += 1
        lps[i] = j
    return lps

def viz_kmp(text: str, pat: str, outdir: str) -> List[str]:
    """生成匹配过程帧图：每一步给出对齐与 i/j 指针。"""
    Path(outdir).mkdir(parents=True, exist_ok=True)
    frames: List[str] = []
    if not pat:
        p = Path(outdir)/"frame_000.png"
        plt.figure(); plt.text(0.1, 0.5, "Empty pattern matches everywhere"); plt.axis("off")
        plt.savefig(p); plt.close(); return [str(p)]
    lps = _lps(pat)
    j = 0; step = 0
    for i, ch in enumerate(text):
        while j and ch != pat[j]:
            # mismatch, jump
            step += 1
            frames.append(_draw(text, pat, i, j, lps, f"mismatch: jump j={lps[j-1]}", outdir, step))
            j = lps[j-1]
        if ch == pat[j]:
            j += 1
            step += 1
            frames.append(_draw(text, pat, i, j-1, lps, "match", outdir, step))
            if j == len(pat):
                step += 1
                frames.append(_draw(text, pat, i, j-1, lps, "pattern found", outdir, step))
                j = lps[j-1]
    return frames

def _draw(text: str, pat: str, i: int, j: int, lps: List[int], msg: str, outdir: str, step: int) -> str:
    fig = plt.figure(figsize=(10, 3))
    ax = plt.gca(); ax.axis("off")
    # Text row
    for idx, ch in enumerate(text):
        ax.text(0.02+idx*0.03, 0.7, ch, fontsize=12)
    # Pattern row aligned at i-j
    off = i - j
    for k, ch in enumerate(pat):
        ax.text(0.02+(off+k)*0.03, 0.4, ch, fontsize=12,
                bbox=dict(facecolor=("lightgreen" if k==j else "white"), alpha=0.5, edgecolor="none"))
    ax.text(0.02, 0.1, f"i={i}, j={j}, note: {msg}", fontsize=10)
    p = Path(outdir) / f"frame_{step:03d}.png"
    fig.tight_layout(); fig.savefig(p); plt.close(fig); return str(p)
