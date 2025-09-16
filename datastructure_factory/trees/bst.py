from __future__ import annotations
from typing import Optional, Generator, Generic, TypeVar
from ..factory.registry import register_adt

T = TypeVar("T")

class _Node(Generic[T]):
    __slots__ = ("key", "left", "right")
    def __init__(self, key: T):
        self.key = key
        self.left: Optional["_Node[T]"] = None
        self.right: Optional["_Node[T]"] = None

@register_adt("bst")
class BST(Generic[T]):
    """二叉搜索树：基础插入/查找/删除。"""

    def __init__(self):
        self.root: Optional[_Node[T]] = None

    def search(self, key: T) -> bool:
        cur = self.root
        while cur:
            if key == cur.key: return True
            cur = cur.left if key < cur.key else cur.right
        return False

    def insert(self, key: T) -> None:
        if not self.root:
            self.root = _Node(key); return
        cur = self.root
        while True:
            if key < cur.key:
                if cur.left: cur = cur.left
                else: cur.left = _Node(key); return
            elif key > cur.key:
                if cur.right: cur = cur.right
                else: cur.right = _Node(key); return
            else:
                return  # 忽略重复

    def _min_node(self, node: _Node[T]) -> _Node[T]:
        while node.left: node = node.left
        return node

    def delete(self, key: T) -> None:
        self.root = self._delete(self.root, key)

    def _delete(self, node: Optional[_Node[T]], key: T) -> Optional[_Node[T]]:
        if not node: return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left: return node.right
            if not node.right: return node.left
            succ = self._min_node(node.right)
            node.key = succ.key
            node.right = self._delete(node.right, succ.key)
        return node

    def inorder(self) -> Generator[T, None, None]:
        def dfs(n: Optional[_Node[T]]):
            if not n: return
            yield from dfs(n.left)
            yield n.key
            yield from dfs(n.right)
        yield from dfs(self.root)
