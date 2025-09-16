# 本科数据结构分析

**User:** Anonymous (harbertparker90526@outlook.com)  
**Created:** 9/16/2025 23:52:08  
**Updated:** 9/17/2025 0:12:47  
**Exported:** 9/17/2025 0:19:16  
**Link:** [https://chatgpt.com/g/g-p-68c390f088dc81918596271e1836757f-deepsearch/c/68c987a6-c6b0-832f-ad1f-d4410e65518a](https://chatgpt.com/g/g-p-68c390f088dc81918596271e1836757f-deepsearch/c/68c987a6-c6b0-832f-ad1f-d4410e65518a)  

## Prompt:
2025-09-16 23:52:04

分析研究 DataStructure 的本科学习内容：

已思考 45s

正在读取文档

用户请求分析数据结构领域的本科学习内容。根据用户需求，我会构建一个结构化大纲，包括模块分解、学习目标、前置知识、课程推荐顺序、项目建议、评估方式、必读书单、常见错误、进阶扩展、与算法的对应关系、复杂度分析、内存管理、并发性、图算法等内容。我会尽量精简，但保持内容全面和重点突出。

用户请求分析数据结构的本科学习内容，要求结构化呈现。我会组织一个有条理的内容，适当使用小节和项目符号。无需浏览器查询，也不需要借助专门工具，只需依照要求提供课程内容的分析，可能会选择表格来呈现，确保简洁明了。

我将根据要求组织一个有结构的学习大纲，包括：

*   目标与要求
*   前置知识
*   核心主题：复杂度与抽象数据类型、数组与字符串、链表变种、栈与队列、堆与优先队列、树类数据结构、图算法、排序算法、字符串算法、内存与缓存行为、并发数据结构等。

这些内容涵盖了数据结构的基础及进阶知识。

我会涵盖高级的学习成果和实际实验：

*   学习成果与难度等级（布卢姆分类法）
*   实验项目建议（如实现库、动态数组、跳表、LRU缓存、图算法库等）
*   评估计划：编码、复杂度证明、口试
*   阅读资料：CLRS、Sedgewick、Goodrich等
*   使用工具与编程语言：C/C++/Java/Python、测试框架等
*   注意陷阱与课程结合：操作系统、数据库、网络等

完成

## Response:
2025-09-16 23:52:53

本科《数据结构》学习内容与路径（工程化视角）
======================

课程定位与目标
-------

数据结构课程位于“程序设计 → 数据结构与算法 → 操作系统/数据库/网络/AI”的核心枢纽位置，目标是让学生掌握以**抽象数据类型（ADT）**为中心的建模方法、以**时间/空间复杂度**与**摊还分析**为核心的性能度量，以及面向工程的**实现与验证**能力。完成后，学生应能选择合适的数据结构解决实际问题，写出正确、可维护、可复用、并具备可测量性能的代码。

先修与能力框架
-------

*   先修能力：一门系统性的编程语言（C/C++/Java/Python 其一）、离散数学（集合、关系、图论基础）、微积分与概率初步、软件基本工程实践（单元测试/调试）。
*   能力层级（由低到高）：能用 → 会实现 → 会分析 → 会优化 → 会权衡并在场景中做架构抉择。

核心知识地图（由“ADT → 实现 → 算法 → 应用”串联）
-------------------------------

1.  **复杂度与分析方法**  
    渐近记号、最坏/平均/摊还复杂度，主定理，递归式，不变量与循环不变式证明，**摊还分析的三法：聚合法、记账法、势能法**。
2.  **线性结构**  
    顺序表/动态数组（容量扩张的摊还 O(1)）、链表（单/双/循环/哨兵/跳表）、栈与队列（含双端队列、单调队列）。
3.  **散列表（哈希表）**  
    哈希函数、负载因子、拉链法/开放定址（线性探测、二次探测、双重散列）、再散列、布隆过滤器与误判率、LRU=哈希表+双向链。
4.  **树结构**  
    二叉搜索树（BST）、平衡搜索树（AVL、红黑树、Treap、Splay 概览）、堆/优先队列（二叉堆、d 叉堆、二项堆/斐波那契堆概念）、区间树/顺序统计树、Trie/前缀树、**B-Tree/B+Tree（外存/数据库）**。
5.  **并查集（Disjoint Set Union, DSU）**  
    路径压缩与按秩合并，近似 O(α(n))。
6.  **图与图算法所需结构**  
    表示（邻接表/邻接矩阵/边集）、遍历（DFS/BFS 的栈/队列实现）、拓扑序、连通性/桥与割点、最短路（Dijkstra/队列优化 Bellman-Ford）、最小生成树（Prim/Kruskal+堆/DSU）。
7.  **排序与选择**  
    比较类：归并/快速/堆排序；线性类：计数/基数/桶；快速选择与中位数；稳定性/原地性/缓存友好性。
8.  **字符串与文本结构（基础版）**  
    模式匹配（KMP、Rabin–Karp）、Trie/后缀数组（LCP 简介）、最小表示；应用到查重/检索。
9.  **内存模型与工程细节（视语言而定）**  
    值/引用/指针/所有权、浅/深拷贝、迭代器失效、缓存局部性（AoS vs SoA）、异常安全与 RAII、泛型与接口设计。
10.  **工程级实践**  
    规格化接口（ADT）、泛型化实现、基准测试（benchmark）、剖析（profiler）、单元测试与属性测试、正确性证明思路与边界用例构造。

15 周建议进度（含实验主线）
---------------

| 周次 | 主题与要点 | 实验/作业（建议语言自选，C/C++/Java/Python） |
| --- | --- | --- |
| 1 | 课程导论；复杂度与递归式；不变量 | 实现动态数组，测扩容摊还成本；主定理练习 |
| 2 | 线性表/链表/双端队列；迭代器失效 | 单链/双链/循环链+哨兵；基准对比 vs 动态数组 |
| 3 | 栈与队列；单调栈/队列应用 | 括号匹配/滑动窗口最大值；性能与边界用例 |
| 4 | 哈希表：设计、碰撞、再散列 | 自实现 HashMap；LRU（哈希+双链） |
| 5 | 树与 BST；旋转与不变量 | 插入/删除的可视化调试；随机测试 |
| 6 | AVL/红黑树/Treap 对比与权衡 | 实现一种平衡树并写顺序统计扩展 |
| 7 | 堆与优先队列；顶 k 与调度 | 二叉堆 vs 多叉堆基准；Top-k/流水线任务调度 |
| 8 | 排序与选择；稳定性/缓存友好 | 自写归并/快速/堆/计数/基数并对比 |
| 9 | 并查集；连通分量/等价类 | DSU + 按秩+路径压缩；动态图连通性实验 |
| 10 | 图存储与遍历；拓扑/强连通 | BFS/DFS 框架抽象；Tarjan/ Kosaraju 概览 |
| 11 | 最短路与最小生成树 | Dijkstra（堆优化）、Kruskal（并查集） |
| 12 | 字符串结构：KMP/RK/Trie | 子串检索、前缀统计；简易搜索引擎雏形 |
| 13 | 外存结构：B-Tree/B+Tree | 迷你“数据库索引”模拟器（页/节点/磁盘访问） |
| 14 | 工程实践：泛型/测试/基准/文档 | GoogleTest/pytest、基准报告与可复现脚本 |
| 15 | 课程项目答辩与综合测试 | 项目展示、复杂度/权衡说明与 code review |

课程项目（梯度化）
---------

*   基础版：实现一套最常用 ADT（动态数组、链表、堆、哈希表、BST/AVL、队列/栈），提供统一接口、文档与单元测试，给出**性能基线**与**复杂度背书**。
*   应用版：选择**真实问题**建模并落地  
    例如：搜索建议/热词统计（Trie+堆）、日志去重与黑名单（布隆过滤器+哈希）、社交网络连通性（DSU）、作业调度/Top-k（堆）、路径规划（图+堆优化 Dijkstra）、LRU/LFU 缓存（链表+哈希/堆）。
*   进阶版：**数据库索引模拟**（B+Tree）、**外排序**（归并+缓冲池）、**字符串索引**（后缀数组+LCP 基线），写明“磁盘 I/O 次数、缓存命中”的工程指标。

评估方式与能力证明
---------

*   知识测验：复杂度推导、摊还分析、数据结构选择题与证明题。
*   编程作业：功能正确性 + 代码质量（风格/注释/接口一致性）+ 单元测试覆盖率。
*   基准报告：合理的工作负载、数据规模与可视化；对比实现与库实现，解释差异与瓶颈。
*   开放题：给定业务场景，比较两种以上数据结构的取舍，写出**选择理由与风险**。

工程化要求与工具链
---------

*   代码规范：Google Style/PEP-8；清晰的 ADT 接口与不变量声明；断言与防御式编程。
*   测试：单元测试（gtest/pytest）、**属性测试**（Hypothesis/rapidcheck），Fuzz 基线。
*   性能：微基准（Google Benchmark/pytest-benchmark）、火焰图/采样剖析（perf/VTune/py-spy）、缓存命中观察（cachegrind）。
*   复现：Makefile/CI 脚本、固定随机种子、数据生成器、README+结果快照。

常见误区与纠偏
-------

*   把“算法对”当作“实现好”：忽视边界条件（空/单元素/极端负载因子）、迭代器失效与并发修改。
*   只谈大 O，不看常数与内存局部性：在工程中缓存友好往往胜过完美的渐近复杂度。
*   平衡树只会“背旋转”：不理解旋转维护的**不变量**与秩统计扩展。
*   哈希表“只要均匀就好”：忽视负载因子与再散列成本、攻击性输入导致退化。
*   图算法当“黑盒”：未根据图稀疏/稠密、权重性质选择存储与算法/堆实现。

进阶与后续课程衔接
---------

*   算法设计与分析（分治、动态规划、贪心、NP 完全性）。
*   数据库系统（索引/B+Tree、缓冲管理、连接算法），信息检索（倒排索引）。
*   操作系统（调度队列、页替换的 LRU/K、内核数据结构）。
*   大数据与外存算法（外排序、缓存/带宽模型、LSM-Tree 概览）。
*   并发数据结构与锁自由结构（课程选讲或后续拓展）。

推荐教材与资源（任选其一主线 + 若干补充）
----------------------

*   《算法导论》与**数据结构章**、Goodrich 系列（C/C++/Java 版本）、Sedgewick & Wayne、Skiena《算法设计手册》。
*   可配合权威库阅读实现：C++ STL、Java Collections、CPython dict/list 实现注释等，用以连接“抽象 → 工程”。

* * *

如果你打算开课或自学，我可以按你熟悉的语言与学期长度，给出**可运行的实验套件**（数据生成器、基准脚本、单元测试模板、CI 配置）与**逐周作业包**；也可以把上面的 15 周计划压缩为 8～10 周强化版，或者为图/字符串/外存方向做加深轨道。

## Prompt:
2025-09-17 00:00:04

核心知识地图（由“ADT → 实现 → 算法 → 应用”串联） ------------------------------- 1. \*\*复杂度与分析方法\*\* 渐近记号、最坏/平均/摊还复杂度，主定理，递归式，不变量与循环不变式证明，\*\*摊还分析的三法：聚合法、记账法、势能法\*\*。 2. \*\*线性结构\*\* 顺序表/动态数组（容量扩张的摊还 O(1)）、链表（单/双/循环/哨兵/跳表）、栈与队列（含双端队列、单调队列）。 3. \*\*散列表（哈希表）\*\* 哈希函数、负载因子、拉链法/开放定址（线性探测、二次探测、双重散列）、再散列、布隆过滤器与误判率、LRU=哈希表+双向链。 4. \*\*树结构\*\* 二叉搜索树（BST）、平衡搜索树（AVL、红黑树、Treap、Splay 概览）、堆/优先队列（二叉堆、d 叉堆、二项堆/斐波那契堆概念）、区间树/顺序统计树、Trie/前缀树、\*\*B-Tree/B+Tree（外存/数据库）\*\*。 5. \*\*并查集（Disjoint Set Union, DSU）\*\* 路径压缩与按秩合并，近似 O(α(n))。 6. \*\*图与图算法所需结构\*\* 表示（邻接表/邻接矩阵/边集）、遍历（DFS/BFS 的栈/队列实现）、拓扑序、连通性/桥与割点、最短路（Dijkstra/队列优化 Bellman-Ford）、最小生成树（Prim/Kruskal+堆/DSU）。 7. \*\*排序与选择\*\* 比较类：归并/快速/堆排序；线性类：计数/基数/桶；快速选择与中位数；稳定性/原地性/缓存友好性。 8. \*\*字符串与文本结构（基础版）\*\* 模式匹配（KMP、Rabin–Karp）、Trie/后缀数组（LCP 简介）、最小表示；应用到查重/检索。 9. \*\*内存模型与工程细节（视语言而定）\*\* 值/引用/指针/所有权、浅/深拷贝、迭代器失效、缓存局部性（AoS vs SoA）、异常安全与 RAII、泛型与接口设计。 10. \*\*工程级实践\*\* 规格化接口（ADT）、泛型化实现、基准测试（benchmark）、剖析（profiler）、单元测试与属性测试、正确性证明思路与边界用例构造。 15 周建议进度（含实验主线） --------------- | 周次 | 主题与要点 | 实验/作业（建议语言自选，C/C++/Java/Python） | | --- | --- | --- | | 1 | 课程导论；复杂度与递归式；不变量 | 实现动态数组，测扩容摊还成本；主定理练习 | | 2 | 线性表/链表/双端队列；迭代器失效 | 单链/双链/循环链+哨兵；基准对比 vs 动态数组 | | 3 | 栈与队列；单调栈/队列应用 | 括号匹配/滑动窗口最大值；性能与边界用例 | | 4 | 哈希表：设计、碰撞、再散列 | 自实现 HashMap；LRU（哈希+双链） | | 5 | 树与 BST；旋转与不变量 | 插入/删除的可视化调试；随机测试 | | 6 | AVL/红黑树/Treap 对比与权衡 | 实现一种平衡树并写顺序统计扩展 | | 7 | 堆与优先队列；顶 k 与调度 | 二叉堆 vs 多叉堆基准；Top-k/流水线任务调度 | | 8 | 排序与选择；稳定性/缓存友好 | 自写归并/快速/堆/计数/基数并对比 | | 9 | 并查集；连通分量/等价类 | DSU + 按秩+路径压缩；动态图连通性实验 | | 10 | 图存储与遍历；拓扑/强连通 | BFS/DFS 框架抽象；Tarjan/ Kosaraju 概览 | | 11 | 最短路与最小生成树 | Dijkstra（堆优化）、Kruskal（并查集） | | 12 | 字符串结构：KMP/RK/Trie | 子串检索、前缀统计；简易搜索引擎雏形 | | 13 | 外存结构：B-Tree/B+Tree | 迷你“数据库索引”模拟器（页/节点/磁盘访问） | | 14 | 工程实践：泛型/测试/基准/文档 | GoogleTest/pytest、基准报告与可复现脚本 | | 15 | 课程项目答辩与综合测试 | 项目展示、复杂度/权衡说明与 code review |

based on knowledge map for datastructure

please build pluggable project using factory mode

construct data category 
using loguru,  matplotlib for logs and visualizations

give me code file by file please!

## Response:
2025-09-17 00:01:56

已思考 1m 47s

我需要为用户构建一个使用工厂模式的可插拔项目，包含数据类别，使用loguru进行日志记录，matplotlib用于可视化。我会创建一个Python包，涵盖常见的数据结构实现。项目将使用工厂模式生成不同的抽象数据类型，并展示它们的性能。

我计划包括“data”子包，用于生成操作序列和随机数据分布；“viz”子包用于生成图表；“factory”用于创建ADT。项目将包含多个模块，如数据结构实现、排序算法、测试、日志配置和CLI工具。虽然用户没有明确要求测试，但我会考虑包括它。

我们可以提供一个最小但功能全面的选择：动态数组、链表、栈、队列、双端队列、哈希表（链式）、LRU（哈希+双向链表）、BST和AVL树、堆、并查集、图表示（邻接表，带BFS/DFS和Dijkstra）、排序算法（快速排序、归并排序、堆排序、计数排序/基数排序）。我们会加入数据生成器、基准模块、运行时与大小的可视化，并使用loguru记录日志。

用户要求“构建数据类别”，可能意味着创建一个存储结果的“data/”文件夹。我打算为日志、图表输出和工作负载样本添加这个“data/”文件夹，不过写入操作不会保证在该目录下进行，因此可以在运行时动态创建目录。另外，我会提供一个“README.md”，但这不是必需的。我将展示代码文件，并且在每个代码块中标注路径和内容，并确保使用中文注释和符合Google风格的文档字符串。

我计划设计整个项目的模块结构。包括注册不同数据结构和算法的工厂模块、基础模块、线性结构、哈希表、树、堆、图、排序算法等，每个模块都应实现基础功能并确保代码简洁明了。例如，`registry.py`用于注册ADT和算法，并通过装饰器简化注册过程。其他模块将按需求提供功能，例如生成随机数组、排序、图算法等。

完成

下面给你一套**可插拔（factory 模式）的数据结构工程项目**，内置 `loguru` 日志与 `matplotlib` 可视化。你可以把下面的文件逐个建立，`pip install -r requirements.txt` 后即可运行 `python -m datastructure_factory.cli.ds_tool --demo sort` 等进行演示与基准测试。

* * *

项目结构（可直接照抄）
-----------

```
datastructure-factory/
├─ requirements.txt
├─ datastructure_factory/
│  ├─ __init__.py
│  ├─ logging_config.py
│  ├─ factory/
│  │  └─ registry.py
│  ├─ core/
│  │  ├─ adt_base.py
│  │  └─ algorithms_base.py
│  ├─ linear/
│  │  ├─ array_list.py
│  │  ├─ linked_list.py
│  │  └─ stack_queue.py
│  ├─ hash/
│  │  ├─ hashmap.py
│  │  └─ lru_cache.py
│  ├─ trees/
│  │  ├─ bst.py
│  │  └─ avl.py
│  ├─ heap/
│  │  └─ binary_heap.py
│  ├─ dsu/
│  │  └─ disjoint_set.py
│  ├─ graph/
│  │  ├─ graph.py
│  │  ├─ shortest_path.py
│  │  └─ mst.py
│  ├─ sorting/
│  │  ├─ comparison.py
│  │  └─ linear_sort.py
│  ├─ strings/
│  │  └─ kmp.py
│  ├─ data/
│  │  └─ workloads.py
│  ├─ bench/
│  │  ├─ benchmark.py
│  │  └─ visualize.py
│  └─ cli/
│     └─ ds_tool.py
└─ (运行中会自动创建) data/logs/ 与 data/reports/
```

* * *

文件逐个给出
------

### `requirements.txt`

```txt
loguru>=0.7.2
matplotlib>=3.8
numpy>=1.26
```

* * *

### `datastructure_factory/__init__.py`

```python
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
```

* * *

### `datastructure_factory/logging_config.py`

```python
from pathlib import Path
from loguru import logger

def setup_logging(log_file: str | None = None) -> None:
    """配置 loguru 日志输出到控制台与文件。

    Args:
        log_file: 可选，日志文件路径。默认写入 data/logs/ds_factory.log
    """
    log_dir = Path("data/logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    logfile = Path(log_file) if log_file else log_dir / "ds_factory.log"

    # 清理默认 handler，避免重复
    logger.remove()
    logger.add(
        sink=lambda msg: print(msg, end=""),
        level="INFO",
        backtrace=False,
        diagnose=False,
        colorize=True,
    )
    logger.add(
        logfile,
        level="DEBUG",
        rotation="10 MB",
        retention="10 days",
        compression="gz",
        enqueue=True,
        backtrace=False,
        diagnose=False,
    )
    logger.debug(f"Logging initialized. File: {logfile}")
```

* * *

### `datastructure_factory/factory/registry.py`

```python
from __future__ import annotations
from typing import Callable, Any, Dict
from loguru import logger

class Registry:
    """通用注册表。支持类或函数的名称->对象映射。"""

    def __init__(self, kind: str):
        self.kind = kind
        self._items: Dict[str, Any] = {}

    def register(self, name: str, obj: Any) -> None:
        key = name.lower()
        if key in self._items:
            logger.warning(f"{self.kind} '{name}' 已存在，将被覆盖。")
        self._items[key] = obj
        logger.debug(f"Registered {self.kind}: {name} -> {obj}")

    def get(self, name: str) -> Any:
        obj = self._items.get(name.lower())
        if obj is None:
            raise KeyError(f"{self.kind} '{name}' 未注册，可用项：{list(self._items)}")
        return obj

    def list_names(self) -> list[str]:
        return sorted(self._items.keys())

ADT_REGISTRY = Registry(kind="ADT")
ALGO_REGISTRY = Registry(kind="ALGO")

def register_adt(name: str | None = None) -> Callable[[Any], Any]:
    """装饰器：注册一个 ADT 类。"""
    def deco(cls: Any) -> Any:
        n = name or cls.__name__
        ADT_REGISTRY.register(n, cls)
        return cls
    return deco

def register_algo(name: str | None = None) -> Callable[[Any], Any]:
    """装饰器：注册一个算法（函数或可调用类）。"""
    def deco(func: Any) -> Any:
        n = name or getattr(func, "__name__", str(func))
        ALGO_REGISTRY.register(n, func)
        return func
    return deco

def get_adt(name: str, **kwargs) -> Any:
    """通过名称实例化 ADT。"""
    cls = ADT_REGISTRY.get(name)
    return cls(**kwargs)

def get_algo(name: str) -> Callable[..., Any]:
    return ALGO_REGISTRY.get(name)

def list_adts() -> list[str]:
    return ADT_REGISTRY.list_names()

def list_algos() -> list[str]:
    return ALGO_REGISTRY.list_names()
```

* * *

### `datastructure_factory/core/adt_base.py`

```python
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable, Generic, TypeVar

T = TypeVar("T")

class ADTBase(ABC, Generic[T]):
    """ADT 抽象基类，统一接口风格。"""

    @abstractmethod
    def __len__(self) -> int: ...

    @abstractmethod
    def clear(self) -> None: ...

    @abstractmethod
    def extend(self, items: Iterable[T]) -> None: ...
```

* * *

### `datastructure_factory/core/algorithms_base.py`

```python
from typing import Protocol, Sequence, Any

class Sorter(Protocol):
    """排序算法协议（duck-typing）。"""

    def __call__(self, arr: Sequence[Any]) -> list[Any]:
        ...
```

* * *

### `datastructure_factory/linear/array_list.py`

```python
from __future__ import annotations
from typing import Generic, TypeVar, Iterable, Optional
from loguru import logger
from ..factory.registry import register_adt
from ..core.adt_base import ADTBase

T = TypeVar("T")

@register_adt("array_list")
class DynamicArray(ADTBase[T], Generic[T]):
    """动态数组：支持容量扩张，摊还 O(1) push/pop。

    Args:
        init_capacity: 初始容量
        data: 初始数据
    """

    def __init__(self, init_capacity: int = 8, data: Optional[Iterable[T]] = None):
        self._n = 0
        self._cap = max(1, init_capacity)
        self._buf = [None] * self._cap  # type: ignore
        logger.debug(f"DynamicArray init cap={self._cap}")
        if data:
            self.extend(data)

    def __len__(self) -> int:
        return self._n

    def _resize(self, new_cap: int) -> None:
        logger.debug(f"Resize from {self._cap} -> {new_cap}")
        tmp = [None] * new_cap  # type: ignore
        for i in range(self._n):
            tmp[i] = self._buf[i]
        self._buf = tmp
        self._cap = new_cap

    def append(self, x: T) -> None:
        if self._n >= self._cap:
            self._resize(self._cap * 2)
        self._buf[self._n] = x
        self._n += 1

    def pop(self) -> T:
        if self._n == 0:
            raise IndexError("pop from empty array")
        self._n -= 1
        x = self._buf[self._n]
        self._buf[self._n] = None
        if 0 < self._n <= self._cap // 4:
            self._resize(max(1, self._cap // 2))
        return x  # type: ignore

    def __getitem__(self, i: int) -> T:
        if not 0 <= i < self._n:
            raise IndexError("index out of range")
        return self._buf[i]  # type: ignore

    def __setitem__(self, i: int, v: T) -> None:
        if not 0 <= i < self._n:
            raise IndexError("index out of range")
        self._buf[i] = v

    def insert(self, i: int, v: T) -> None:
        if not 0 <= i <= self._n:
            raise IndexError("index out of range")
        if self._n >= self._cap:
            self._resize(self._cap * 2)
        for j in range(self._n, i, -1):
            self._buf[j] = self._buf[j-1]
        self._buf[i] = v
        self._n += 1

    def delete(self, i: int) -> T:
        if not 0 <= i < self._n:
            raise IndexError("index out of range")
        v = self._buf[i]
        for j in range(i, self._n - 1):
            self._buf[j] = self._buf[j+1]
        self._n -= 1
        self._buf[self._n] = None
        if 0 < self._n <= self._cap // 4:
            self._resize(max(1, self._cap // 2))
        return v  # type: ignore

    def clear(self) -> None:
        self._n = 0
        self._buf = [None] * max(1, self._cap)

    def extend(self, items: Iterable[T]) -> None:
        for x in items:
            self.append(x)
```

* * *

### `datastructure_factory/linear/linked_list.py`

```python
from __future__ import annotations
from typing import Generic, TypeVar, Optional, Iterable
from ..factory.registry import register_adt
from ..core.adt_base import ADTBase

T = TypeVar("T")

class _Node(Generic[T]):
    __slots__ = ("val", "next", "prev")
    def __init__(self, val: T):
        self.val = val
        self.next: Optional["_Node[T]"] = None
        self.prev: Optional["_Node[T]"] = None

@register_adt("singly_linked_list")
class SinglyLinkedList(ADTBase[T]):
    def __init__(self, data: Optional[Iterable[T]] = None):
        self.head: Optional[_Node[T]] = None
        self._n = 0
        if data:
            self.extend(data)

    def __len__(self) -> int: return self._n
    def clear(self) -> None:
        self.head = None
        self._n = 0

    def extend(self, items: Iterable[T]) -> None:
        for x in items:
            self.append(x)

    def append(self, x: T) -> None:
        node = _Node(x)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self._n += 1

    def delete_value(self, x: T) -> bool:
        prev = None
        cur = self.head
        while cur:
            if cur.val == x:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                self._n -= 1
                return True
            prev, cur = cur, cur.next
        return False

@register_adt("deque_list")
class DequeList(ADTBase[T]):
    """双向链表实现的双端队列。"""
    def __init__(self, data: Optional[Iterable[T]] = None):
        self.head: Optional[_Node[T]] = None
        self.tail: Optional[_Node[T]] = None
        self._n = 0
        if data:
            self.extend(data)

    def __len__(self) -> int: return self._n
    def clear(self) -> None:
        self.head = self.tail = None
        self._n = 0

    def extend(self, items: Iterable[T]) -> None:
        for x in items:
            self.push_back(x)

    def push_front(self, x: T) -> None:
        node = _Node(x)
        node.next = self.head
        if self.head:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node
        self._n += 1

    def push_back(self, x: T) -> None:
        node = _Node(x)
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self._n += 1

    def pop_front(self) -> T:
        if not self.head: raise IndexError("pop_front from empty")
        node = self.head
        self.head = node.next
        if self.head: self.head.prev = None
        else: self.tail = None
        self._n -= 1
        return node.val

    def pop_back(self) -> T:
        if not self.tail: raise IndexError("pop_back from empty")
        node = self.tail
        self.tail = node.prev
        if self.tail: self.tail.next = None
        else: self.head = None
        self._n -= 1
        return node.val
```

* * *

### `datastructure_factory/linear/stack_queue.py`

```python
from __future__ import annotations
from typing import Generic, TypeVar, Iterable, Optional
from ..factory.registry import register_adt
from ..core.adt_base import ADTBase

T = TypeVar("T")

@register_adt("stack")
class Stack(ADTBase[T]):
    def __init__(self, data: Optional[Iterable[T]] = None):
        self._buf: list[T] = []
        if data: self.extend(data)
    def __len__(self) -> int: return len(self._buf)
    def clear(self) -> None: self._buf.clear()
    def extend(self, items: Iterable[T]) -> None:
        self._buf.extend(items)
    def push(self, x: T) -> None: self._buf.append(x)
    def pop(self) -> T: return self._buf.pop()
    def peek(self) -> T: return self._buf[-1]

@register_adt("queue")
class Queue(ADTBase[T]):
    """数组 + 头指针实现的队列，避免 O(n) 的 pop(0)。"""
    def __init__(self, data: Optional[Iterable[T]] = None):
        self._buf: list[T] = []
        self._head = 0
        if data: self.extend(data)
    def __len__(self) -> int: return len(self._buf) - self._head
    def clear(self) -> None:
        self._buf.clear(); self._head = 0
    def extend(self, items: Iterable[T]) -> None:
        self._buf.extend(items)
    def push(self, x: T) -> None: self._buf.append(x)
    def pop(self) -> T:
        if self._head >= len(self._buf): raise IndexError("pop from empty")
        x = self._buf[self._head]; self._head += 1
        # 定期压缩空间
        if self._head > 32 and self._head * 2 > len(self._buf):
            self._buf = self._buf[self._head:]; self._head = 0
        return x
```

* * *

### `datastructure_factory/hash/hashmap.py`

```python
from __future__ import annotations
from typing import Generic, TypeVar, Iterable, Optional, Iterator, Tuple
from ..factory.registry import register_adt
from ..core.adt_base import ADTBase

K = TypeVar("K")
V = TypeVar("V")

@register_adt("hash_map")
class HashMap(ADTBase[Tuple[K, V]], Generic[K, V]):
    """拉链法哈希表，支持自动扩容/缩容。"""

    def __init__(self, capacity: int = 8, load_factor: float = 0.75):
        self._n = 0
        self._cap = max(4, capacity)
        self._load = load_factor
        self._buckets: list[list[tuple[K, V]]] = [[] for _ in range(self._cap)]

    def __len__(self) -> int: return self._n
    def clear(self) -> None:
        self._n = 0
        self._buckets = [[] for _ in range(self._cap)]

    def extend(self, items: Iterable[tuple[K, V]]) -> None:
        for k, v in items: self.put(k, v)

    def _idx(self, key: K) -> int:
        return (hash(key) & 0x7FFFFFFF) % self._cap

    def _rehash(self, new_cap: int) -> None:
        old_items = [(k, v) for bucket in self._buckets for (k, v) in bucket]
        self._cap = max(4, new_cap)
        self._buckets = [[] for _ in range(self._cap)]
        self._n = 0
        for k, v in old_items:
            self.put(k, v)

    def put(self, key: K, val: V) -> None:
        i = self._idx(key)
        bucket = self._buckets[i]
        for idx, (k, _) in enumerate(bucket):
            if k == key:
                bucket[idx] = (key, val)
                return
        bucket.append((key, val))
        self._n += 1
        if self._n > self._cap * self._load:
            self._rehash(self._cap * 2)

    def get(self, key: K, default: Optional[V] = None) -> Optional[V]:
        i = self._idx(key)
        for k, v in self._buckets[i]:
            if k == key:
                return v
        return default

    def remove(self, key: K) -> bool:
        i = self._idx(key)
        bucket = self._buckets[i]
        for idx, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(idx)
                self._n -= 1
                if self._cap > 8 and self._n < self._cap * 0.25:
                    self._rehash(self._cap // 2)
                return True
        return False

    def items(self) -> Iterator[tuple[K, V]]:
        for bucket in self._buckets:
            for kv in bucket:
                yield kv
```

* * *

### `datastructure_factory/hash/lru_cache.py`

```python
from __future__ import annotations
from typing import Generic, TypeVar, Optional, Dict
from ..factory.registry import register_adt

K = TypeVar("K")
V = TypeVar("V")

class _Node(Generic[K, V]):
    __slots__ = ("k", "v", "prev", "next")
    def __init__(self, k: K, v: V):
        self.k, self.v = k, v
        self.prev: Optional["_Node[K, V]"] = None
        self.next: Optional["_Node[K, V]"] = None

@register_adt("lru_cache")
class LRUCache(Generic[K, V]):
    """LRU: 哈希表 + 双向链表，get/put O(1)。"""

    def __init__(self, capacity: int = 128):
        self.cap = capacity
        self.map: Dict[K, _Node[K, V]] = {}
        # 伪头尾哨兵
        self.head = _Node(None, None)  # type: ignore
        self.tail = _Node(None, None)  # type: ignore
        self.head.next = self.tail; self.tail.prev = self.head

    def _remove(self, node: _Node[K, V]) -> None:
        p, n = node.prev, node.next
        assert p and n
        p.next = n; n.prev = p

    def _append_front(self, node: _Node[K, V]) -> None:
        n1 = self.head.next
        assert n1
        node.prev = self.head; node.next = n1
        self.head.next = node; n1.prev = node

    def get(self, k: K) -> Optional[V]:
        node = self.map.get(k)
        if not node: return None
        self._remove(node); self._append_front(node)
        return node.v

    def put(self, k: K, v: V) -> None:
        node = self.map.get(k)
        if node:
            node.v = v
            self._remove(node); self._append_front(node)
            return
        node = _Node(k, v)
        self.map[k] = node
        self._append_front(node)
        if len(self.map) > self.cap:
            # 淘汰尾部
            last = self.tail.prev
            assert last and last is not self.head
            self._remove(last)
            self.map.pop(last.k, None)
```

* * *

### `datastructure_factory/trees/bst.py`

```python
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
```

* * *

### `datastructure_factory/trees/avl.py`

```python
from __future__ import annotations
from typing import Optional, Generic, TypeVar
from ..factory.registry import register_adt

T = TypeVar("T")

class _N(Generic[T]):
    __slots__ = ("k","l","r","h")
    def __init__(self, k: T):
        self.k = k; self.l: Optional["_N[T]"] = None; self.r: Optional["_N[T]"] = None; self.h = 1

def _h(n: Optional[_N[T]]) -> int: return n.h if n else 0
def _upd(n: _N[T]) -> None: n.h = max(_h(n.l), _h(n.r)) + 1
def _bf(n: _N[T]) -> int: return _h(n.l) - _h(n.r)

def _rot_r(y: _N[T]) -> _N[T]:
    x = y.l; assert x
    T2 = x.r
    x.r = y; y.l = T2
    _upd(y); _upd(x); return x

def _rot_l(x: _N[T]) -> _N[T]:
    y = x.r; assert y
    T2 = y.l
    y.l = x; x.r = T2
    _upd(x); _upd(y); return y

def _balance(n: _N[T]) -> _N[T]:
    _upd(n)
    b = _bf(n)
    if b > 1:
        if _bf(n.l) < 0: n.l = _rot_l(n.l)  # type: ignore
        return _rot_r(n)
    if b < -1:
        if _bf(n.r) > 0: n.r = _rot_r(n.r)  # type: ignore
        return _rot_l(n)
    return n

@register_adt("avl")
class AVL(Generic[T]):
    def __init__(self):
        self.root: Optional[_N[T]] = None

    def insert(self, k: T) -> None:
        def _ins(n: Optional[_N[T]], k: T) -> _N[T]:
            if not n: return _N(k)
            if k < n.k: n.l = _ins(n.l, k)
            elif k > n.k: n.r = _ins(n.r, k)
            else: return n
            return _balance(n)
        self.root = _ins(self.root, k)

    def _min(self, n: _N[T]) -> _N[T]:
        while n.l: n = n.l
        return n

    def delete(self, k: T) -> None:
        def _del(n: Optional[_N[T]], k: T) -> Optional[_N[T]]:
            if not n: return None
            if k < n.k: n.l = _del(n.l, k)
            elif k > n.k: n.r = _del(n.r, k)
            else:
                if not n.l: return n.r
                if not n.r: return n.l
                s = self._min(n.r)
                n.k = s.k
                n.r = _del(n.r, s.k)
            return _balance(n) if n else None
        self.root = _del(self.root, k)
```

* * *

### `datastructure_factory/heap/binary_heap.py`

```python
from __future__ import annotations
from typing import Generic, TypeVar, Iterable, Callable, Optional
from ..factory.registry import register_adt

T = TypeVar("T")

@register_adt("min_heap")
class MinHeap(Generic[T]):
    """二叉最小堆，使用数组实现。"""
    def __init__(self, data: Optional[Iterable[T]] = None, key: Callable[[T], T] | None = None):
        self.a: list[T] = []
        self.key = key or (lambda x: x)
        if data:
            self.a = list(data)
            for i in reversed(range(len(self.a)//2)):
                self._down(i)

    def __len__(self) -> int: return len(self.a)
    def clear(self) -> None: self.a.clear()
    def extend(self, items: Iterable[T]) -> None:
        for x in items: self.push(x)

    def _less(self, i: int, j: int) -> bool:
        return self.key(self.a[i]) < self.key(self.a[j])

    def _swap(self, i: int, j: int) -> None:
        self.a[i], self.a[j] = self.a[j], self.a[i]

    def _up(self, i: int) -> None:
        while i > 0:
            p = (i - 1) // 2
            if self._less(i, p):
                self._swap(i, p); i = p
            else: break

    def _down(self, i: int) -> None:
        n = len(self.a)
        while True:
            l, r = 2*i+1, 2*i+2
            m = i
            if l < n and self._less(l, m): m = l
            if r < n and self._less(r, m): m = r
            if m == i: break
            self._swap(i, m); i = m

    def push(self, x: T) -> None:
        self.a.append(x); self._up(len(self.a)-1)

    def pop(self) -> T:
        if not self.a: raise IndexError("pop from empty heap")
        self._swap(0, len(self.a)-1)
        x = self.a.pop()
        if self.a: self._down(0)
        return x

    def peek(self) -> T:
        if not self.a: raise IndexError("peek from empty heap")
        return self.a[0]
```

* * *

### `datastructure_factory/dsu/disjoint_set.py`

```python
from __future__ import annotations
from typing import Dict, Hashable
from ..factory.registry import register_adt

@register_adt("dsu")
class DisjointSet:
    """并查集（路径压缩 + 按秩合并），近似 O(α(n))。"""
    def __init__(self):
        self.parent: Dict[Hashable, Hashable] = {}
        self.rank: Dict[Hashable, int] = {}

    def find(self, x: Hashable) -> Hashable:
        if x not in self.parent:
            self.parent[x] = x; self.rank[x] = 0
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: Hashable, y: Hashable) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx == ry: return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
```

* * *

### `datastructure_factory/graph/graph.py`

```python
from __future__ import annotations
from typing import Dict, List, Hashable, Iterable
from ..factory.registry import register_adt

@register_adt("graph")
class Graph:
    """邻接表表示无向/有向图。"""
    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adj: Dict[Hashable, List[Hashable]] = {}

    def add_edge(self, u: Hashable, v: Hashable) -> None:
        self.adj.setdefault(u, []).append(v)
        if not self.directed:
            self.adj.setdefault(v, []).append(u)

    def vertices(self) -> Iterable[Hashable]:
        return self.adj.keys()

    def neighbors(self, u: Hashable) -> Iterable[Hashable]:
        return self.adj.get(u, [])
```

* * *

### `datastructure_factory/graph/shortest_path.py`

```python
from __future__ import annotations
import heapq
from typing import Dict, Tuple, Hashable, Iterable
from ..factory.registry import register_algo

@register_algo("dijkstra")
def dijkstra(adj_w: Dict[Hashable, Dict[Hashable, float]], src: Hashable) -> Tuple[Dict[Hashable, float], Dict[Hashable, Hashable]]:
    """堆优化 Dijkstra。adj_w: {u: {v: w}}"""
    dist: Dict[Hashable, float] = {src: 0.0}
    prev: Dict[Hashable, Hashable] = {}
    pq: list[tuple[float, Hashable]] = [(0.0, src)]
    vis: set[Hashable] = set()

    while pq:
        d, u = heapq.heappop(pq)
        if u in vis: continue
        vis.add(u)
        for v, w in adj_w.get(u, {}).items():
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd; prev[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, prev
```

* * *

### `datastructure_factory/graph/mst.py`

```python
from __future__ import annotations
from typing import List, Tuple, Hashable
from ..factory.registry import register_algo
from ..dsu.disjoint_set import DisjointSet

@register_algo("kruskal")
def kruskal(n_vertices: int, edges: List[Tuple[float, Hashable, Hashable]]) -> Tuple[float, List[Tuple[float, Hashable, Hashable]]]:
    """Kruskal 最小生成树，edges: (w,u,v)"""
    dsu = DisjointSet()
    weight = 0.0
    mst: List[Tuple[float, Hashable, Hashable]] = []
    for w,u,v in sorted(edges):
        if dsu.find(u) != dsu.find(v):
            dsu.union(u,v)
            mst.append((w,u,v))
            weight += w
    return weight, mst
```

* * *

### `datastructure_factory/sorting/comparison.py`

```python
from __future__ import annotations
from typing import Sequence, Any, List
from ..factory.registry import register_algo

@register_algo("quicksort")
def quicksort(a: Sequence[Any]) -> List[Any]:
    arr = list(a)
    def sort(l: int, r: int) -> None:
        if l >= r: return
        i, j = l, r
        pivot = arr[(l+r)//2]
        while i <= j:
            while arr[i] < pivot: i += 1
            while arr[j] > pivot: j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1; j -= 1
        if l < j: sort(l, j)
        if i < r: sort(i, r)
    sort(0, len(arr)-1)
    return arr

@register_algo("mergesort")
def mergesort(a: Sequence[Any]) -> List[Any]:
    arr = list(a)
    def msort(x: List[Any]) -> List[Any]:
        if len(x) <= 1: return x
        mid = len(x)//2
        L = msort(x[:mid]); R = msort(x[mid:])
        i=j=0; out=[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]: out.append(L[i]); i+=1
            else: out.append(R[j]); j+=1
        out.extend(L[i:]); out.extend(R[j:])
        return out
    return msort(arr)

@register_algo("heapsort")
def heapsort(a: Sequence[Any]) -> List[Any]:
    import heapq
    h = list(a); heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]
```

* * *

### `datastructure_factory/sorting/linear_sort.py`

```python
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
```

* * *

### `datastructure_factory/strings/kmp.py`

```python
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
```

* * *

### `datastructure_factory/data/workloads.py`

```python
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
```

* * *

### `datastructure_factory/bench/benchmark.py`

```python
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
```

* * *

### `datastructure_factory/bench/visualize.py`

```python
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
```

* * *

### `datastructure_factory/cli/ds_tool.py`

```python
from __future__ import annotations
import argparse
from loguru import logger
from ..factory.registry import get_algo, list_algos, list_adts, get_adt
from ..bench.benchmark import bench_sorters
from ..bench.visualize import plot_curves
from ..data.workloads import random_int_array, ops_for_hashmap, ops_for_dsu

def demo_sort(args: argparse.Namespace) -> None:
    algos = {name: get_algo(name) for name in args.algos}
    sizes = [int(s) for s in args.sizes]
    res = bench_sorters(algos, sizes, seed=args.seed, repeats=args.repeats)
    png = plot_curves(res, sizes, "Sorting Benchmark", "sorting_bench.png")
    logger.success(f"图已保存：{png}")

def demo_hashmap(args: argparse.Namespace) -> None:
    hm = get_adt("hash_map")
    ops = list(ops_for_hashmap(args.puts, args.gets, key_space=args.key_space, seed=args.seed))
    hit = miss = 0
    for op in ops:
        if op[0] == "put":
            _, k, v = op; hm.put(k, v)
        else:
            _, k = op
            hit += 1 if hm.get(k) is not None else 0
            miss += 1 if hm.get(k) is None else 0
    logger.info(f"HashMap 状态：size={len(list(hm.items()))} 命中={hit} 未命中={miss}")

def demo_dsu(args: argparse.Namespace) -> None:
    dsu = get_adt("dsu")
    for op in ops_for_dsu(args.ops, seed=args.seed):
        if op[0] == "union":
            _, a, b = op; dsu.union(a, b)
        else:
            _, x = op; _ = dsu.find(x)
    logger.success("DSU 演示完成。")

def demo_lru(args: argparse.Namespace) -> None:
    lru = get_adt("lru_cache", capacity=args.capacity)
    for i in range(args.ops):
        lru.put(i, i*i)
        _ = lru.get(i-1)
    logger.success("LRU 演示完成。")

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser("DataStructure Factory CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("sort", help="排序基准")
    sp.add_argument("--algos", nargs="+", default=["quicksort", "mergesort", "heapsort"])
    sp.add_argument("--sizes", nargs="+", default=["1000", "5000", "10000"])
    sp.add_argument("--seed", type=int, default=42)
    sp.add_argument("--repeats", type=int, default=3)
    sp.set_defaults(func=demo_sort)

    hp = sub.add_parser("hashmap", help="哈希表演示")
    hp.add_argument("--puts", type=int, default=5000)
    hp.add_argument("--gets", type=int, default=5000)
    hp.add_argument("--key-space", type=int, default=10000)
    hp.add_argument("--seed", type=int, default=123)
    hp.set_defaults(func=demo_hashmap)

    dp = sub.add_parser("dsu", help="并查集演示")
    dp.add_argument("--ops", type=int, default=2000)
    dp.add_argument("--seed", type=int, default=7)
    dp.set_defaults(func=demo_dsu)

    lp = sub.add_parser("lru", help="LRU 缓存演示")
    lp.add_argument("--capacity", type=int, default=128)
    lp.add_argument("--ops", type=int, default=1000)
    lp.set_defaults(func=demo_lru)

    sub.add_parser("list", help="列出已注册 ADT/算法").set_defaults(
        func=lambda _: (
            print("ADTs:", list_adts()),
            print("ALGOs:", list_algos()),
        )
    )
    return p

def main() -> None:
    args = build_parser().parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
```

* * *

使用方式
----

1.  安装依赖

```bash
pip install -r requirements.txt
```

2.  运行排序基准并画图（自动输出到 `data/reports/sorting_bench.png`）

```bash
python -m datastructure_factory.cli.ds_tool sort --algos quicksort mergesort heapsort --sizes 1000 5000 10000 20000 --repeats 3
```

3.  哈希表 / 并查集 / LRU 演示

```bash
python -m datastructure_factory.cli.ds_tool hashmap --puts 3000 --gets 3000
python -m datastructure_factory.cli.ds_tool dsu --ops 5000
python -m datastructure_factory.cli.ds_tool lru --capacity 256 --ops 2000
```

* * *

如果你想把图结构（BFS/DFS/拓扑）、字符串（KMP）或 AVL/BST 的**可视化**也做成报告，我可以补一版 `viz_*.py` 与 CLI 子命令，生成结构演化快照或步进动画（matplotlib 动图）。还需要把**更多结构**（如跳表、Trie/B+Tree、布隆过滤器、Treap、红黑树）纳入 factory，只要说一声，我直接给你追加同风格文件。

## Prompt:
2025-09-17 00:11:37

1. 如果你想把图结构（BFS/DFS/拓扑）、字符串（KMP）或 AVL/BST 的可视化也做成报告，我可以补一版 viz_*.py 与 CLI 子命令，生成结构演化快照或步进动画（matplotlib 动图）
2. 需要把更多结构（如跳表、Trie/B+Tree、布隆过滤器、Treap、红黑树）纳入 factory

add and update please

## Response:
2025-09-17 00:12:46

已思考 1m 3s

我们需要扩展项目，包括可视化模块和其他数据结构，例如跳表、Trie/B+树、布隆过滤器、Treap、红黑树。代码要按文件提供，包含工厂注册功能。避免过长的代码，但必须实现基本操作；需要使用matplotlib来做可视化，并更新命令行接口以生成报告或动画。

我们将保存编号系列的PNG帧到data/reports目录，并添加总结表或静态进度图。这更简单，符合约定。还会更新cli/ds\_tool.py，增加viz-graph、viz-tree和viz-kmp命令。同时，我们要新增若干模块文件，例如红黑树、Treap、简单B树、Trie、布隆过滤器以及跳表。

KMP可视化：展示模式滑动和LPS，我们可以为每个处理的字符生成一个帧。对于BST/AVL，可通过每次插入后展示树，并为树的坐标计算布局。跳表和布隆过滤器使用适合的结构，如`bytearray`和简单的自定义哈希函数来执行。

Treap是一个随机化优先队列，红黑树我们实现插入修正，删除可以选择性添加。虽然用户期望完整操作，删除虽然挺长，但可以不做，或者先提供插入和查找。红黑树将实现插入和删除，按照CLRS风格进行。

完成

太好了！基于你之前的工程骨架，我给你**两大更新**：

1.  新增三套可视化模块（BFS/DFS/拓扑、KMP、BST/AVL/RBT/Treap 动态）与对应 CLI 子命令，自动把帧图保存到 `data/reports/`。
2.  新增更多数据结构：**跳表、Trie、B-Tree（插入/查找）、布隆过滤器、Treap、红黑树（RBT）**，全部纳入 factory 可插拔注册。

下面是**更新后的项目树**与**新增/修改文件**（直接按文件创建或覆盖即可）。

* * *

更新后的项目结构（新增/变更标注 ⭐）
===================

```
datastructure-factory/
├─ requirements.txt
├─ datastructure_factory/
│  ├─ __init__.py                        ⭐（更新：导入新模块以触发注册）
│  ├─ logging_config.py
│  ├─ factory/
│  │  └─ registry.py
│  ├─ core/
│  │  ├─ adt_base.py
│  │  └─ algorithms_base.py
│  ├─ linear/
│  │  ├─ array_list.py
│  │  ├─ linked_list.py
│  │  └─ stack_queue.py
│  ├─ hash/
│  │  ├─ hashmap.py
│  │  └─ lru_cache.py
│  ├─ trees/
│  │  ├─ bst.py
│  │  ├─ avl.py
│  │  ├─ treap.py                        ⭐ 新增
│  │  ├─ rbtree.py                       ⭐ 新增
│  │  └─ btree.py                        ⭐ 新增（B-Tree 插入/查找）
│  ├─ heap/
│  │  └─ binary_heap.py
│  ├─ dsu/
│  │  └─ disjoint_set.py
│  ├─ graph/
│  │  ├─ graph.py
│  │  ├─ shortest_path.py
│  │  └─ mst.py
│  ├─ sorting/
│  │  ├─ comparison.py
│  │  └─ linear_sort.py
│  ├─ strings/
│  │  ├─ kmp.py
│  │  └─ trie.py                         ⭐ 新增
│  ├─ probabilistic/
│  │  └─ bloom.py                        ⭐ 新增（布隆过滤器）
│  ├─ skiplist/
│  │  └─ skip_list.py                    ⭐ 新增（跳表）
│  ├─ data/
│  │  └─ workloads.py
│  ├─ bench/
│  │  ├─ benchmark.py
│  │  ├─ visualize.py
│  │  ├─ viz_graph.py                    ⭐ 新增（BFS/DFS/拓扑 动态帧）
│  │  ├─ viz_kmp.py                      ⭐ 新增（KMP 动态帧）
│  │  └─ viz_trees.py                    ⭐ 新增（BST/AVL/RBT/Treap 插入演化）
│  └─ cli/
│     └─ ds_tool.py                      ⭐（更新：添加可视化子命令）
└─ data/
   ├─ logs/     (运行时自动创建)
   └─ reports/  (运行时自动创建)
```

* * *

1) 修改：`datastructure_factory/__init__.py`
-----------------------------------------

```python
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
```

* * *

2) 新增：`datastructure_factory/skiplist/skip_list.py`（跳表）
-------------------------------------------------------

```python
from __future__ import annotations
import random
from typing import Generic, TypeVar, Optional, List, Iterable
from ..factory.registry import register_adt

K = TypeVar("K")
V = TypeVar("V")

class _Node(Generic[K, V]):
    __slots__ = ("key", "val", "forw")
    def __init__(self, key: Optional[K], val: Optional[V], level: int):
        self.key = key
        self.val = val
        self.forw: List[Optional["_Node[K, V]"]] = [None]*(level+1)

@register_adt("skip_list")
class SkipList(Generic[K, V]):
    """跳表：期望 O(log n) 查找/插入/删除。"""
    def __init__(self, max_level: int = 16, p: float = 0.5):
        self.max_level = max_level
        self.p = p
        self.level = 0
        self.head = _Node[K, V](None, None, max_level)
        self._n = 0

    def __len__(self) -> int: return self._n
    def clear(self) -> None:
        self.level = 0
        self.head = _Node(None, None, self.max_level)
        self._n = 0
    def extend(self, items: Iterable[tuple[K, V]]) -> None:
        for k, v in items: self.insert(k, v)

    def _rand_level(self) -> int:
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def search(self, key: K) -> Optional[V]:
        cur = self.head
        for i in reversed(range(self.level+1)):
            while cur.forw[i] and cur.forw[i].key < key:
                cur = cur.forw[i]
        cur = cur.forw[0]
        return cur.val if cur and cur.key == key else None

    def insert(self, key: K, val: V) -> None:
        update = [None]*(self.max_level+1)
        cur = self.head
        for i in reversed(range(self.level+1)):
            while cur.forw[i] and cur.forw[i].key < key:
                cur = cur.forw[i]
            update[i] = cur
        cur = cur.forw[0]
        if cur and cur.key == key:
            cur.val = val
            return
        lvl = self._rand_level()
        if lvl > self.level:
            for i in range(self.level+1, lvl+1):
                update[i] = self.head
            self.level = lvl
        node = _Node(key, val, lvl)
        for i in range(lvl+1):
            node.forw[i] = update[i].forw[i]
            update[i].forw[i] = node
        self._n += 1

    def delete(self, key: K) -> bool:
        update = [None]*(self.max_level+1)
        cur = self.head
        for i in reversed(range(self.level+1)):
            while cur.forw[i] and cur.forw[i].key < key:
                cur = cur.forw[i]
            update[i] = cur
        cur = cur.forw[0]
        if not cur or cur.key != key:
            return False
        for i in range(self.level+1):
            if update[i].forw[i] != cur: break
            update[i].forw[i] = cur.forw[i]
        while self.level > 0 and self.head.forw[self.level] is None:
            self.level -= 1
        self._n -= 1
        return True
```

* * *

3) 新增：`datastructure_factory/strings/trie.py`（Trie）
---------------------------------------------------

```python
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
```

* * *

4) 新增：`datastructure_factory/probabilistic/bloom.py`（布隆过滤器）
-----------------------------------------------------------

```python
from __future__ import annotations
from typing import Iterable, Hashable, List
from ..factory.registry import register_adt

@register_adt("bloom")
class BloomFilter:
    """布隆过滤器（简单位图版）。"""
    def __init__(self, m_bits: int = 1<<20, k_hashes: int = 7, seeds: Iterable[int] | None = None):
        assert m_bits > 0 and k_hashes > 0
        self.m = m_bits
        self.k = k_hashes
        self.bits = bytearray((m_bits + 7) // 8)
        if seeds is None:
            self.seeds = [146959810, 2166136261, 2654435761, 40503, 1315423911, 374761393, 86028157][:self.k]
        else:
            ss = list(seeds)
            assert len(ss) >= self.k
            self.seeds = ss[:self.k]

    def __len__(self) -> int: return self.m
    def clear(self) -> None: self.bits = bytearray(len(self.bits))
    def extend(self, items: Iterable[Hashable]) -> None:
        for x in items: self.add(x)

    def _hashes(self, x: Hashable) -> List[int]:
        h = hash(x)
        return [((h ^ s) * 11400714819323198485 & 0xFFFFFFFFFFFFFFFF) % self.m for s in self.seeds]

    def _setbit(self, i: int) -> None:
        self.bits[i >> 3] |= (1 << (i & 7))
    def _getbit(self, i: int) -> bool:
        return (self.bits[i >> 3] >> (i & 7)) & 1 == 1

    def add(self, x: Hashable) -> None:
        for i in self._hashes(x): self._setbit(int(i))

    def contains(self, x: Hashable) -> bool:
        return all(self._getbit(int(i)) for i in self._hashes(x))
```

* * *

5) 新增：`datastructure_factory/trees/treap.py`
--------------------------------------------

```python
from __future__ import annotations
import random
from typing import Optional, Generic, TypeVar
from ..factory.registry import register_adt

T = TypeVar("T")

class _N(Generic[T]):
    __slots__ = ("key","prio","l","r")
    def __init__(self, key: T, prio: int):
        self.key = key; self.prio = prio
        self.l: Optional["_N[T]"] = None
        self.r: Optional["_N[T]"] = None

def _rot_r(y: _N[T]) -> _N[T]:
    x = y.l; assert x
    y.l = x.r; x.r = y; return x

def _rot_l(x: _N[T]) -> _N[T]:
    y = x.r; assert y
    x.r = y.l; y.l = x; return y

@register_adt("treap")
class Treap(Generic[T]):
    """Treap（树堆）：按 key BST、按 prio 堆。"""
    def __init__(self, seed: int = 42):
        self.root: Optional[_N[T]] = None
        self.rng = random.Random(seed)

    def _ins(self, n: Optional[_N[T]], k: T) -> _N[T]:
        if not n: return _N(k, self.rng.randint(1, 10**9))
        if k < n.key:
            n.l = self._ins(n.l, k)
            if n.l and n.l.prio < n.prio: n = _rot_r(n)
        elif k > n.key:
            n.r = self._ins(n.r, k)
            if n.r and n.r.prio < n.prio: n = _rot_l(n)
        return n

    def insert(self, k: T) -> None:
        self.root = self._ins(self.root, k)

    def _del(self, n: Optional[_N[T]], k: T) -> Optional[_N[T]]:
        if not n: return None
        if k < n.key: n.l = self._del(n.l, k)
        elif k > n.key: n.r = self._del(n.r, k)
        else:
            if not n.l: return n.r
            if not n.r: return n.l
            if n.l.prio < n.r.prio:
                n = _rot_r(n); n.r = self._del(n.r, k)
            else:
                n = _rot_l(n); n.l = self._del(n.l, k)
        return n

    def delete(self, k: T) -> None:
        self.root = self._del(self.root, k)

    def search(self, k: T) -> bool:
        cur = self.root
        while cur:
            if k == cur.key: return True
            cur = cur.l if k < cur.key else cur.r
        return False
```

* * *

6) 新增：`datastructure_factory/trees/rbtree.py`（红黑树，插入/删除）
--------------------------------------------------------

```python
from __future__ import annotations
from typing import Optional, Generic, TypeVar
from ..factory.registry import register_adt

T = TypeVar("T")
RED, BLACK = 0, 1

class _N(Generic[T]):
    __slots__ = ("key","left","right","parent","color")
    def __init__(self, key: T, color: int = RED):
        self.key = key
        self.left: Optional["_N[T]"] = None
        self.right: Optional["_N[T]"] = None
        self.parent: Optional["_N[T]"] = None
        self.color = color

def _is_red(n: Optional[_N[T]]) -> bool: return bool(n and n.color == RED)

@register_adt("rbtree")
class RBTree(Generic[T]):
    """红黑树（CLRS 风格，支持插入与删除）。"""
    def __init__(self):
        self.root: Optional[_N[T]] = None

    # 旋转
    def _rot_l(self, x: _N[T]) -> None:
        y = x.right; assert y
        x.right = y.left
        if y.left: y.left.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x is x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left = x; x.parent = y

    def _rot_r(self, y: _N[T]) -> None:
        x = y.left; assert x
        y.left = x.right
        if x.right: x.right.parent = y
        x.parent = y.parent
        if not y.parent: self.root = x
        elif y is y.parent.left: y.parent.left = x
        else: y.parent.right = x
        x.right = y; y.parent = x

    # 插入
    def insert(self, key: T) -> None:
        z = _N(key, RED)
        y: Optional[_N[T]] = None
        x = self.root
        while x:
            y = x
            x = x.left if z.key < x.key else x.right
        z.parent = y
        if not y: self.root = z
        elif z.key < y.key: y.left = z
        else: y.right = z
        self._insert_fix(z)

    def _insert_fix(self, z: _N[T]) -> None:
        while z.parent and _is_red(z.parent):
            if z.parent is z.parent.parent.left:  # type: ignore
                y = z.parent.parent.right  # 叔
                if _is_red(y):
                    z.parent.color = BLACK; y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z is z.parent.right:
                        z = z.parent
                        self._rot_l(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._rot_r(z.parent.parent)
            else:
                y = z.parent.parent.left
                if _is_red(y):
                    z.parent.color = BLACK; y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self._rot_r(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._rot_l(z.parent.parent)
        if self.root: self.root.color = BLACK

    # 删除
    def _transplant(self, u: _N[T], v: Optional[_N[T]]) -> None:
        if not u.parent: self.root = v
        elif u is u.parent.left: u.parent.left = v
        else: u.parent.right = v
        if v: v.parent = u.parent

    def _min(self, n: _N[T]) -> _N[T]:
        while n.left: n = n.left
        return n

    def delete(self, key: T) -> None:
        z = self._search_node(key)
        if not z: return
        y = z; y_orig_color = y.color
        if not z.left:
            x = z.right
            self._transplant(z, z.right)
        elif not z.right:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._min(z.right)
            y_orig_color = y.color
            x = y.right
            if y.parent is z:
                if x: x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right; y.right.parent = y  # type: ignore
            self._transplant(z, y)
            y.left = z.left; y.left.parent = y  # type: ignore
            y.color = z.color
        if y_orig_color == BLACK:
            self._delete_fix(x, parent=(y.parent if y else None))

    def _delete_fix(self, x: Optional[_N[T]], parent: Optional[_N[T]]) -> None:
        while (x is not self.root) and (not _is_red(x)):
            if x is (parent.left if parent else None):
                w = parent.right if parent else None
                if _is_red(w):
                    w.color = BLACK; parent.color = RED
                    self._rot_l(parent); w = parent.right
                if (not _is_red(w.left if w else None)) and (not _is_red(w.right if w else None)):
                    if w: w.color = RED
                    x = parent; parent = x.parent if x else None
                else:
                    if not _is_red(w.right if w else None):
                        if w and w.left: w.left.color = BLACK
                        if w: w.color = RED
                        if parent: self._rot_r(w)  # type: ignore
                        w = parent.right if parent else None
                    if w: w.color = parent.color if parent else BLACK
                    if parent: parent.color = BLACK
                    if w and w.right: w.right.color = BLACK
                    if parent: self._rot_l(parent)
                    x = self.root; parent = None
            else:
                w = parent.left if parent else None
                if _is_red(w):
                    w.color = BLACK; parent.color = RED
                    self._rot_r(parent); w = parent.left
                if (not _is_red(w.left if w else None)) and (not _is_red(w.right if w else None)):
                    if w: w.color = RED
                    x = parent; parent = x.parent if x else None
                else:
                    if not _is_red(w.left if w else None):
                        if w and w.right: w.right.color = BLACK
                        if w: w.color = RED
                        if parent: self._rot_l(w)  # type: ignore
                        w = parent.left if parent else None
                    if w: w.color = parent.color if parent else BLACK
                    if parent: parent.color = BLACK
                    if w and w.left: w.left.color = BLACK
                    if parent: self._rot_r(parent)
                    x = self.root; parent = None
        if x: x.color = BLACK

    def _search_node(self, key: T) -> Optional[_N[T]]:
        cur = self.root
        while cur:
            if key == cur.key: return cur
            cur = cur.left if key < cur.key else cur.right
        return None

    def search(self, key: T) -> bool:
        return self._search_node(key) is not None
```

* * *

7) 新增：`datastructure_factory/trees/btree.py`（B-Tree：插入/查找）
----------------------------------------------------------

```python
from __future__ import annotations
from typing import List, Optional, Generic, TypeVar
from ..factory.registry import register_adt

T = TypeVar("T")

class _Node(Generic[T]):
    def __init__(self, t: int, leaf: bool):
        self.t = t
        self.leaf = leaf
        self.keys: List[T] = []
        self.child: List["_Node[T]"] = []

@register_adt("btree")
class BTree(Generic[T]):
    """B-Tree（最小度 t >= 2），支持 search / insert。"""
    def __init__(self, t: int = 3):
        assert t >= 2, "t >= 2"
        self.t = t
        self.root = _Node[T](t, True)

    def search(self, k: T, x: Optional[_Node[T]] = None) -> bool:
        if x is None: x = self.root
        i = 0
        while i < len(x.keys) and k > x.keys[i]: i += 1
        if i < len(x.keys) and k == x.keys[i]: return True
        if x.leaf: return False
        return self.search(k, x.child[i])

    def insert(self, k: T) -> None:
        r = self.root
        if len(r.keys) == 2*self.t - 1:
            s = _Node[T](self.t, False)
            self.root = s
            s.child.append(r)
            self._split_child(s, 0)
            self._insert_nonfull(s, k)
        else:
            self._insert_nonfull(r, k)

    def _split_child(self, x: _Node[T], i: int) -> None:
        t = self.t
        y = x.child[i]
        z = _Node[T](t, y.leaf)
        x.child.insert(i+1, z)
        x.keys.insert(i, y.keys[t-1])
        z.keys = y.keys[t:(2*t-1)]
        y.keys = y.keys[0:t-1]
        if not y.leaf:
            z.child = y.child[t:(2*t)]
            y.child = y.child[0:t]

    def _insert_nonfull(self, x: _Node[T], k: T) -> None:
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(k)
            i = len(x.keys) - 2
            while i >= 0 and x.keys[i] > k:
                x.keys[i+1] = x.keys[i]; i -= 1
            x.keys[i+1] = k
        else:
            while i >= 0 and k < x.keys[i]: i -= 1
            i += 1
            if len(x.child[i].keys) == 2*self.t - 1:
                self._split_child(x, i)
                if k > x.keys[i]: i += 1
            self._insert_nonfull(x.child[i], k)
```

* * *

8) 新增：`datastructure_factory/bench/viz_graph.py`（BFS/DFS/拓扑 动态帧）
----------------------------------------------------------------

```python
from __future__ import annotations
from typing import Dict, List, Hashable, Tuple, Iterable, Set
from pathlib import Path
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def _circle_layout(nodes: List[Hashable]) -> Dict[Hashable, Tuple[float, float]]:
    n = len(nodes)
    return {u: (math.cos(2*math.pi*i/n), math.sin(2*math.pi*i/n)) for i, u in enumerate(nodes)}

def _draw_frame(pos, edges, color_map, step, outdir: Path, title: str):
    fig = plt.figure(figsize=(6,6))
    ax = plt.gca(); ax.axis("off")
    # edges
    for (u,v) in edges:
        x1,y1 = pos[u]; x2,y2 = pos[v]
        ax.plot([x1,x2],[y1,y2], alpha=0.3)
    # nodes
    for u,(x,y) in pos.items():
        c = color_map.get(u, "lightgray")
        ax.scatter([x],[y], s=600, edgecolors="k", zorder=3, c=c)
        ax.text(x, y, str(u), ha="center", va="center", fontsize=12, zorder=4)
    ax.set_title(title)
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / f"frame_{step:03d}.png"
    fig.tight_layout()
    fig.savefig(path); plt.close(fig)
    return str(path)

def viz_bfs(adj: Dict[Hashable, Iterable[Hashable]], src: Hashable, outdir: str) -> List[str]:
    nodes = sorted(set(adj.keys()) | {v for u in adj for v in adj[u]})
    pos = _circle_layout(nodes)
    edges = set()
    for u in adj:
        for v in adj[u]:
            edges.add(tuple(sorted((u,v))))
    frames = []
    color = {}
    q: List[Hashable] = [src]
    seen: Set[Hashable] = {src}
    step = 0
    frames.append(_draw_frame(pos, edges, color, step, Path(outdir), f"BFS start @ {src}"))
    while q:
        u = q.pop(0)
        color[u] = "tab:green"
        step += 1
        frames.append(_draw_frame(pos, edges, color, step, Path(outdir), f"BFS visit {u}"))
        for v in adj.get(u, []):
            if v not in seen:
                seen.add(v); q.append(v)
                color[v] = "tab:orange"
                step += 1
                frames.append(_draw_frame(pos, edges, color, step, Path(outdir), f"BFS discover {v}"))
    return frames

def viz_dfs(adj: Dict[Hashable, Iterable[Hashable]], src: Hashable, outdir: str) -> List[str]:
    nodes = sorted(set(adj.keys()) | {v for u in adj for v in adj[u]})
    pos = _circle_layout(nodes)
    edges = set()
    for u in adj:
        for v in adj[u]:
            edges.add(tuple(sorted((u,v))))
    frames = []
    color = {}
    seen: Set[Hashable] = set()
    step = 0
    stack: List[Tuple[Hashable, int]] = [(src, 0)]
    frames.append(_draw_frame(pos, edges, color, step, Path(outdir), f"DFS start @ {src}"))
    while stack:
        u, it = stack.pop()
        if u not in seen:
            seen.add(u); color[u] = "tab:blue"
            step += 1
            frames.append(_draw_frame(pos, edges, color, step, Path(outdir), f"DFS visit {u}"))
            nbrs = list(adj.get(u, []))
            for v in reversed(nbrs):
                if v not in seen:
                    color[v] = color.get(v, "tab:orange")
                    step += 1
                    frames.append(_draw_frame(pos, edges, color, step, Path(outdir), f"DFS push {v}"))
                    stack.append((v, 0))
    return frames

def viz_topo_kahn(adj: Dict[Hashable, Iterable[Hashable]], outdir: str) -> List[str]:
    indeg = {u: 0 for u in adj}
    for u in adj:
        for v in adj[u]:
            indeg[v] = indeg.get(v, 0) + 1
            if v not in adj: adj[v] = []
    nodes = list(adj.keys())
    pos = _circle_layout(nodes)
    edges = set()
    for u in adj:
        for v in adj[u]:
            edges.add((u, v))  # 有向就不排序

    frames = []
    q = [u for u in nodes if indeg.get(u, 0) == 0]
    taken = []
    color = {u: ("tab:orange" if indeg.get(u,0)==0 else "lightgray") for u in nodes}
    step = 0
    frames.append(_draw_frame(pos, edges, color, step, Path(outdir), "Topo sort: init zero-indegree"))
    while q:
        u = q.pop(0)
        taken.append(u); color[u] = "tab:green"
        step += 1
        frames.append(_draw_frame(pos, edges, color, step, Path(outdir), f"Take {u}"))
        for v in adj.get(u, []):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v); color[v] = "tab:orange"
                step += 1
                frames.append(_draw_frame(pos, edges, color, step, Path(outdir), f"Unlock {v}"))
    return frames
```

* * *

9) 新增：`datastructure_factory/bench/viz_kmp.py`
----------------------------------------------

```python
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
```

* * *

10) 新增：`datastructure_factory/bench/viz_trees.py`（插入演化：BST/AVL/RBT/Treap）
-------------------------------------------------------------------------

```python
from __future__ import annotations
from typing import Any, Optional, List, Tuple, Callable
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def _get_children(node: Any) -> Tuple[Optional[Any], Optional[Any]]:
    # 兼容不同节点字段：BST(key,left,right)；AVL(k,l,r)；RBT(key,left,right,color)；Treap(key,l,r)
    if node is None: return None, None
    if hasattr(node, "left") or hasattr(node, "right"):
        return getattr(node, "left", None), getattr(node, "right", None)
    return getattr(node, "l", None), getattr(node, "r", None)

def _get_key(node: Any) -> Any:
    return getattr(node, "key", getattr(node, "k", None))

def _get_color(node: Any) -> str:
    # 红黑：node.color == 0 红；其它树统一蓝色
    if hasattr(node, "color"):
        return "tab:red" if getattr(node, "color") == 0 else "k"
    return "tab:blue"

def _layout(root: Any) -> dict[Any, Tuple[float, float]]:
    # 中序编号 -> x，深度 -> y
    x = 0
    pos: dict[Any, Tuple[float, float]] = {}
    def dfs(n: Any, d: int):
        nonlocal x
        if not n: return
        l, r = _get_children(n)
        dfs(l, d+1)
        pos[n] = (x, -d)
        x += 1
        dfs(r, d+1)
    dfs(root, 0)
    # scale
    return {n: (px, py) for n,(px,py) in pos.items()}

def _edges(root: Any) -> List[Tuple[Any, Any]]:
    es: List[Tuple[Any, Any]] = []
    def go(n: Any):
        if not n: return
        l, r = _get_children(n)
        if l: es.append((n, l)); go(l)
        if r: es.append((n, r)); go(r)
    go(root); return es

def draw_tree(root: Any, title: str, outpath: str) -> str:
    Path(outpath).parent.mkdir(parents=True, exist_ok=True)
    pos = _layout(root)
    es = _edges(root)
    fig = plt.figure(figsize=(8, 4.5))
    ax = plt.gca(); ax.axis("off")
    for u,v in es:
        x1,y1 = pos[u]; x2,y2 = pos[v]
        ax.plot([x1,x2],[y1,y2], color="0.6")
    for n,(x,y) in pos.items():
        ax.scatter([x],[y], s=600, facecolors="white", edgecolors=_get_color(n), linewidths=2)
        ax.text(x, y, str(_get_key(n)), ha="center", va="center")
    ax.set_title(title)
    fig.tight_layout(); fig.savefig(outpath); plt.close(fig)
    return outpath

def viz_insert_evolution(make_tree: Callable[[], Any], inserts: List[int], outdir: str, name: str) -> List[str]:
    frames: List[str] = []
    t = make_tree()
    for step, k in enumerate(inserts, start=1):
        # 支持不同树的 insert 接口
        if hasattr(t, "insert"): t.insert(k)
        elif hasattr(t, "put"): t.put(k)
        else: raise RuntimeError("Tree insert interface not found.")
        path = Path(outdir) / f"{name}_step_{step:03d}.png"
        root = getattr(t, "root", None)
        frames.append(draw_tree(root, f"{name}: insert {k}", str(path)))
    return frames
```

* * *

11) 修改：`datastructure_factory/cli/ds_tool.py`（新增 viz 子命令）
---------------------------------------------------------

```python
from __future__ import annotations
import argparse
from loguru import logger
from ..factory.registry import get_algo, list_algos, list_adts, get_adt
from ..bench.benchmark import bench_sorters
from ..bench.visualize import plot_curves
from ..data.workloads import random_int_array, ops_for_hashmap, ops_for_dsu
from ..bench.viz_graph import viz_bfs, viz_dfs, viz_topo_kahn
from ..bench.viz_kmp import viz_kmp
from ..bench.viz_trees import viz_insert_evolution

def demo_sort(args: argparse.Namespace) -> None:
    algos = {name: get_algo(name) for name in args.algos}
    sizes = [int(s) for s in args.sizes]
    res = bench_sorters(algos, sizes, seed=args.seed, repeats=args.repeats)
    png = plot_curves(res, sizes, "Sorting Benchmark", "sorting_bench.png")
    logger.success(f"图已保存：{png}")

def demo_hashmap(args: argparse.Namespace) -> None:
    hm = get_adt("hash_map")
    ops = list(ops_for_hashmap(args.puts, args.gets, key_space=args.key_space, seed=args.seed))
    hit = miss = 0
    for op in ops:
        if op[0] == "put":
            _, k, v = op; hm.put(k, v)
        else:
            _, k = op
            val = hm.get(k)
            hit += 1 if val is not None else 0
            miss += 1 if val is None else 0
    logger.info(f"HashMap 状态：size={len(list(hm.items()))} 命中={hit} 未命中={miss}")

def demo_dsu(args: argparse.Namespace) -> None:
    dsu = get_adt("dsu")
    for op in ops_for_dsu(args.ops, seed=args.seed):
        if op[0] == "union":
            _, a, b = op; dsu.union(a, b)
        else:
            _, x = op; _ = dsu.find(x)
    logger.success("DSU 演示完成。")

def demo_lru(args: argparse.Namespace) -> None:
    lru = get_adt("lru_cache", capacity=args.capacity)
    for i in range(args.ops):
        lru.put(i, i*i)
        _ = lru.get(i-1)
    logger.success("LRU 演示完成。")

# === 新增：可视化 ===
def demo_viz_graph(args: argparse.Namespace) -> None:
    # 简单随机图或示例图
    adj = {}
    if args.example == "toy":
        adj = {1:[2,3], 2:[4], 3:[4,5], 4:[], 5:[4]} if args.directed else {1:[2,3], 2:[1,4], 3:[1,4,5], 4:[2,3], 5:[3]}
    else:
        import random
        n = args.n; p = args.p
        nodes = list(range(1, n+1))
        adj = {u: [] for u
```

Network connection lost. Attempting to reconnect…



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)