from __future__ import annotations
from typing import List
from ..factory.registry import register_algo

@register_algo("kmp_search")
def kmp_search(text: str, pat: str) -> List[int]:
    if not pat: return list(range(len(text)+1))
    # 预处理 lps
    lps = [0]*len(pat)
    j = 0
    for i in range(1, len(pat)):
        while j and pat[i] != pat[j]:
            j = lps[j-1]
        if pat[i] == pat[j]:
            j += 1
        lps[i] = j
    # 匹配
    res: List[int] = []
    j = 0
    for i,ch in enumerate(text):
        while j and ch != pat[j]:
            j = lps[j-1]
        if ch == pat[j]:
            j += 1
            if j == len(pat):
                res.append(i - j + 1)
                j = lps[j-1]
    return res
