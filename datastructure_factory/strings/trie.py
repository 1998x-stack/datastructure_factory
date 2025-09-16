from __future__ import annotations
from typing import Dict
from ..factory.registry import register_adt

class _Node:
    __slots__ = ("ch", "end")
    def __init__(self):
        self.ch: Dict[str, _Node] = {}
        self.end: bool = False

@register_adt("trie")
class Trie:
    """Trie 前缀树：insert/search/starts_with"""
    def __init__(self): self.root = _Node()
    def __len__(self) -> int: return -1  # 非线性尺寸，不在此定义
    def clear(self) -> None: self.root = _Node()
    def extend(self, items): 
        for s in items: self.insert(s)

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.ch.setdefault(c, _Node())
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.ch: return False
            cur = cur.ch[c]
        return cur.end

    def starts_with(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.ch: return False
            cur = cur.ch[c]
        return True
