from __future__ import annotations
from time import perf_counter
from typing import Callable, Any, Dict
from pathlib import Path
import numpy as np
from loguru import logger

def timeit(func: Callable[..., Any], *args, repeats: int = 3, **kwargs) -> float:
    """多次运行取最小值，减少噪声。"""
    best = float("inf")
    for _ in range(repeats):
        t0 = perf_counter()
        func(*args, **kwargs)
        dt = perf_counter() - t0
        best = min(best, dt)
    return best

def bench_sorters(sorters: Dict[str, Callable[[list[int]], list[int]]],
                  sizes: list[int], seed: int = 42, repeats: int = 3) -> Dict[str, list[float]]:
    """对若干排序算法进行规模-时间基准测试。"""
    rng = np.random.default_rng(seed)
    results: Dict[str, list[float]] = {name: [] for name in sorters}
    for n in sizes:
        arr = rng.integers(0, 1_000_000, size=n).tolist()
        for name, sorter in sorters.items():
            logger.info(f"[sort-bench] algo={name} n={n}")
            t = timeit(sorter, arr, repeats=repeats)
            results[name].append(t)
    outdir = Path("data/reports"); outdir.mkdir(parents=True, exist_ok=True)
    logger.success(f"排序基准完成，结果点数：{[(k, len(v)) for k,v in results.items()]}")
    return results
