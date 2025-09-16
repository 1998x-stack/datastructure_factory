"""DataStructure Factory — 可插拔数据结构与算法工程套件。"""

from .logging_config import setup_logging
from .factory.registry import (
    get_adt, get_algo, list_adts, list_algos,
    ADT_REGISTRY, ALGO_REGISTRY,
)

setup_logging()

# 原有导入
from .linear import array_list, linked_list, stack_queue  # noqa: F401
from .hash import hashmap, lru_cache  # noqa: F401
from .trees import bst, avl  # noqa: F401
from .heap import binary_heap  # noqa: F401
from .dsu import disjoint_set  # noqa: F401
from .graph import graph, shortest_path, mst  # noqa: F401
from .sorting import comparison, linear_sort  # noqa: F401
from .strings import kmp  # noqa: F401
from .bench import benchmark, visualize  # noqa: F401

# 新增结构（触发注册）
from .trees import treap, rbtree, btree  # noqa: F401
from .strings import trie  # noqa: F401
from .probabilistic import bloom  # noqa: F401
from .skiplist import skip_list  # noqa: F401

__all__ = [
    "get_adt", "get_algo", "list_adts", "list_algos",
    "ADT_REGISTRY", "ALGO_REGISTRY",
]
