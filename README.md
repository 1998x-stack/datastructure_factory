# datastructure_factory

> 可插拔的**数据结构与算法工厂库**——科研级别的 ADT 实现 + 可视化 + 基准测试。

## 📌 项目概述

`datastructure_factory` 是一个模块化、工厂模式组织的数据结构与算法库，涵盖**线性结构、树、图、哈希、堆、跳表、并查集、字符串、排序、概率结构**等经典 ADT，并附带可视化与基准测试工具，适合教学、研究与面试复习。

## 🗂️ 目录结构

```
datastructure_factory/
├─ datastructure_factory/
│  ├─ core/           # ADT 与算法抽象基类
│  ├─ linear/         # 数组、链表、栈与队列
│  ├─ trees/          # BST / AVL / Treap / B-Tree / 红黑树
│  ├─ graph/          # 图、最短路、最小生成树
│  ├─ hash/           # 哈希表、LRU 缓存
│  ├─ heap/           # 二叉堆
│  ├─ dsu/            # 并查集
│  ├─ skiplist/       # 跳表
│  ├─ sorting/        # 线性/比较排序
│  ├─ strings/        # KMP、Trie
│  ├─ probabilistic/  # Bloom Filter
│  ├─ bench/          # 基准测试与可视化（树/图/KMP）
│  ├─ cli/ds_tool.py  # 命令行工具
│  └─ logging_config.py
└─ data/              # 示例数据
```

## 🚀 快速开始

```bash
pip install -r requirements.txt
# 运行命令行工具
python -m datastructure_factory.cli.ds_tool --help
```

学习材料见 `ChatGPT-本科数据结构分析.md`。

## 📄 License

MIT