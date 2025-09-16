"""DataStructure Factory — 可插拔数据结构与算法工程套件。"""

from .logging_config import setup_logging
from .factory.registry import (
    get_adt, get_algo, list_adts, list_algos,
    ADT_REGISTRY, ALGO_REGISTRY,
)

# 初始化日志
setup_logging()

# 显式导入以触发注册（避免延迟导入导致的“未注册”问题）
# 线性结构
from .linear import array_list, linked_list, stack_queue  # noqa: F401
# 哈希与缓存
from .hash import hashmap, lru_cache  # noqa: F401
# 树与堆
from .trees import bst, avl  # noqa: F401
from .heap import binary_heap  # noqa: F401
# 并查集
from .dsu import disjoint_set  # noqa: F401
# 图
from .graph import graph, shortest_path, mst  # noqa: F401
# 排序与字符串
from .sorting import comparison, linear_sort  # noqa: F401
from .strings import kmp  # noqa: F401
# 基准与可视化（用于 CLI）
from .bench import benchmark, visualize  # noqa: F401

__all__ = [
    "get_adt", "get_algo", "list_adts", "list_algos",
    "ADT_REGISTRY", "ALGO_REGISTRY",
]
