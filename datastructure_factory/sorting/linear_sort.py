from __future__ import annotations
from typing import Sequence, List
from ..factory.registry import register_algo

@register_algo("counting_sort")
def counting_sort(a: Sequence[int]) -> List[int]:
    if not a: return []
    mn, mx = min(a), max(a)
    if mn < 0: raise ValueError("counting_sort 仅支持非负整数")
    cnt = [0] * (mx - mn + 1)
    for x in a: cnt[x - mn] += 1
    out: List[int] = []
    for i, c in enumerate(cnt):
        out.extend([i + mn] * c)
    return out

@register_algo("radix_sort")
def radix_sort(a: Sequence[int], base: int = 10) -> List[int]:
    if not a: return []
    arr = list(a)
    exp = 1
    mx = max(arr)
    while mx // exp > 0:
        # 计数排序按位
        cnt = [0]*base
        out = [0]*len(arr)
        for x in arr: cnt[(x // exp) % base] += 1
        for i in range(1, base): cnt[i] += cnt[i-1]
        for x in reversed(arr):
            d = (x // exp) % base
            cnt[d] -= 1
            out[cnt[d]] = x
        arr = out
        exp *= base
    return arr
