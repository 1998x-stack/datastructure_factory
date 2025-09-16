from __future__ import annotations
from typing import Iterable, Literal
import numpy as np

def random_int_array(n: int, low: int = 0, high: int = 10_000, seed: int = 42) -> list[int]:
    """生成长度 n 的随机整数数组。"""
    rng = np.random.default_rng(seed)
    return rng.integers(low, high, size=n).tolist()

def ops_for_hashmap(n_put: int, n_get: int, key_space: int = 100_000, seed: int = 123):
    """生成哈希表操作序列：('put', k, v) 或 ('get', k)。"""
    rng = np.random.default_rng(seed)
    for _ in range(n_put):
        k = int(rng.integers(0, key_space)); v = int(rng.integers(0, 1_000_000))
        yield ("put", k, v)
    for _ in range(n_get):
        k = int(rng.integers(0, key_space))
        yield ("get", k)

def ops_for_dsu(n: int, seed: int = 7):
    """生成并查集合并/查询操作。"""
    rng = np.random.default_rng(seed)
    for _ in range(n):
        a, b = int(rng.integers(0, 1000)), int(rng.integers(0, 1000))
        yield ("union", a, b)
        if rng.random() < 0.5:
            x = int(rng.integers(0, 1000))
            yield ("find", x)
