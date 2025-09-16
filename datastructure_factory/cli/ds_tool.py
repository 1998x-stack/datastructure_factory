from __future__ import annotations

#TODO: correct
import argparse
from typing import List, Dict, Any, Sequence, Optional
from loguru import logger

# Factory/bench/data imports
from ..factory.registry import get_algo, list_algos, list_adts, get_adt
from ..bench.benchmark import bench_sorters
from ..bench.visualize import plot_curves
from ..data.workloads import random_int_array, ops_for_hashmap, ops_for_dsu
# Viz modules
from ..bench.viz_graph import viz_bfs, viz_dfs, viz_topo_kahn
from ..bench.viz_kmp import viz_kmp
from ..bench.viz_trees import viz_insert_evolution


# ------------------------------
# Demo commands
# ------------------------------
def demo_sort(args: argparse.Namespace) -> None:
    algos = {name: get_algo(name) for name in args.algos}
    sizes = [int(s) for s in args.sizes]
    res = bench_sorters(algos, sizes, seed=args.seed, repeats=args.repeats)
    png = plot_curves(res, sizes, "Sorting Benchmark", args.out)
    logger.success(f"图已保存：{png}")


def demo_hashmap(args: argparse.Namespace) -> None:
    hm = get_adt("hash_map")
    ops = list(ops_for_hashmap(args.puts, args.gets, key_space=args.key_space, seed=args.seed))
    hit = miss = 0
    for op in ops:
        if op[0] == "put":
            _, k, v = op
            hm.put(k, v)
        else:
            _, k = op
            val = hm.get(k)
            hit += 1 if val is not None else 0
            miss += 1 if val is None else 0
    size = 0
    try:
        size = len(list(hm.items()))
    except Exception:
        try:
            size = len(hm)
        except Exception:
            pass
    logger.info(f"HashMap 状态：size={size} 命中={hit} 未命中={miss}")


def demo_dsu(args: argparse.Namespace) -> None:
    dsu = get_adt("dsu")
    for op in ops_for_dsu(args.ops, seed=args.seed):
        if op[0] == "union":
            _, a, b = op
            dsu.union(a, b)
        else:
            _, x = op
            _ = dsu.find(x)
    logger.success("DSU 演示完成。")


def demo_lru(args: argparse.Namespace) -> None:
    lru = get_adt("lru_cache", capacity=args.capacity)
    for i in range(args.ops):
        lru.put(i, i * i)
        _ = lru.get(i - 1)
    logger.success("LRU 演示完成。")


# ------------------------------
# Viz commands
# ------------------------------
def _gen_random_graph(n: int, p: float, directed: bool, seed: Optional[int]) -> Dict[int, List[int]]:
    import random
    rng = random.Random(seed)
    nodes = list(range(1, n + 1))
    adj = {u: [] for u in nodes}
    for u in nodes:
        for v in nodes:
            if u == v:
                continue
            if rng.random() < p:
                adj[u].append(v)
                if not directed:
                    adj[v].append(u)
    if not directed:
        # de-duplicate undirected adjacency
        for u in nodes:
            adj[u] = sorted(set(adj[u]))
    return adj


def demo_viz_graph(args: argparse.Namespace) -> None:
    """可视化 BFS/DFS/拓扑排序（Kahn）。"""
    # 构造图
    if args.example == "toy":
        if args.directed:
            adj = {1: [2, 3], 2: [4], 3: [4, 5], 4: [], 5: [4]}
        else:
            adj = {1: [2, 3], 2: [1, 4], 3: [1, 4, 5], 4: [2, 3], 5: [3]}
    else:
        adj = _gen_random_graph(args.n, args.p, args.directed, args.seed)

    out = args.out
    fmt = args.fmt
    fps = args.fps

    logger.info(f"图节点数={len(adj)}, directed={args.directed}, 起点={args.start}, 输出={out} ({fmt})")
    try:
        if args.algo == "bfs":
            saved = viz_bfs(adj, start=args.start, out=out, fmt=fmt, fps=fps, directed=args.directed)
        elif args.algo == "dfs":
            saved = viz_dfs(adj, start=args.start, out=out, fmt=fmt, fps=fps, directed=args.directed)
        elif args.algo in ("topo", "topo_kahn"):
            if not args.directed:
                logger.warning("拓扑排序通常用于有向无环图（DAG），此处将按 directed=True 处理。")
            saved = viz_topo_kahn(adj, out=out, fmt=fmt, fps=fps)
        else:
            raise ValueError(f"未知图算法：{args.algo}")
        logger.success(f"可视化完成：{saved}")
    except TypeError:
        # 兼容不同签名
        if args.algo == "bfs":
            saved = viz_bfs(adj, args.start, out, fmt, fps)
        elif args.algo == "dfs":
            saved = viz_dfs(adj, args.start, out, fmt, fps)
        else:
            saved = viz_topo_kahn(adj, out, fmt, fps)
        logger.success(f"可视化完成：{saved}")


def demo_viz_kmp(args: argparse.Namespace) -> None:
    """可视化 KMP 模式匹配过程。"""
    text = args.text
    pattern = args.pattern
    out = args.out
    fmt = args.fmt
    fps = args.fps
    logger.info(f"KMP 可视化：|text|={len(text)} |pattern|={len(pattern)} 输出={out} ({fmt})")
    try:
        saved = viz_kmp(text=text, pattern=pattern, out=out, fmt=fmt, fps=fps)
    except TypeError:
        saved = viz_kmp(text, pattern, out, fmt, fps)
    logger.success(f"可视化完成：{saved}")


def demo_viz_tree(args: argparse.Namespace) -> None:
    """可视化树（BST/AVL/RBT/Treap）插入演化。"""
    ds_name = args.kind.lower()
    if ds_name not in ("bst", "avl", "rbt", "rbtree", "treap"):
        raise ValueError("kind 仅支持：bst / avl / rbt(rbtree) / treap")
    if ds_name == "rbtree":
        ds_name = "rbt"

    # 生成序列
    seq: List[int] = []
    if args.seq:
        for part in args.seq.split(","):
            part = part.strip()
            if not part:
                continue
            try:
                seq.append(int(part))
            except ValueError:
                logger.warning(f"忽略非整数：{part}")
    else:
        import random
        rng = random.Random(args.seed)
        low, high = args.range
        seq = [rng.randint(low, high) for _ in range(args.n)]
    logger.info(f"{ds_name.upper()} 插入序列：{seq}")

    # 渲染
    try:
        saved = viz_insert_evolution(kind=ds_name, sequence=seq, out=args.out, fmt=args.fmt, fps=args.fps)
    except TypeError:
        saved = viz_insert_evolution(ds_name, seq, args.out, args.fmt, args.fps)
    logger.success(f"可视化完成：{saved}")


# ------------------------------
# Utility commands
# ------------------------------
def cmd_list(args: argparse.Namespace) -> None:
    print("== 可用算法 ==")
    for name in sorted(list_algos()):
        print(f" - {name}")
    print("\n== 可用 ADT ==")
    for name in sorted(list_adts()):
        print(f" - {name}")


# ------------------------------
# Argparse wiring
# ------------------------------
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="ds-tool", description="DataStructure Factory CLI")
    p.add_argument("--seed", type=int, default=42, help="随机种子（默认 42）")

    sub = p.add_subparsers(dest="cmd", required=True)

    # list
    sp_list = sub.add_parser("list", help="列出工厂已注册的算法与 ADT")
    sp_list.set_defaults(func=cmd_list)

    # sort
    sp_sort = sub.add_parser("sort", help="排序算法基准测试并绘图")
    sp_sort.add_argument("--algos", nargs="+", required=True, help="待比较的排序算法名")
    sp_sort.add_argument("--sizes", nargs="+", required=True, help="输入规模，如 1e3 2e3 5e3 1e4")
    sp_sort.add_argument("--repeats", type=int, default=3, help="每个规模重复次数")
    sp_sort.add_argument("--out", default="sorting_bench.png", help="输出图片路径（.png）")
    sp_sort.set_defaults(func=demo_sort)

    # hashmap
    sp_hm = sub.add_parser("hashmap", help="HashMap put/get 演示")
    sp_hm.add_argument("--puts", type=int, default=1000, help="put 次数")
    sp_hm.add_argument("--gets", type=int, default=1000, help="get 次数")
    sp_hm.add_argument("--key-space", type=int, default=2000, help="键空间上限（含）")
    sp_hm.set_defaults(func=demo_hashmap)

    # dsu
    sp_dsu = sub.add_parser("dsu", help="并查集 (DSU) 演示")
    sp_dsu.add_argument("--ops", type=int, default=1000, help="随机操作数（union/find 混合）")
    sp_dsu.set_defaults(func=demo_dsu)

    # lru
    sp_lru = sub.add_parser("lru", help="LRU Cache 演示")
    sp_lru.add_argument("--capacity", type=int, default=16, help="容量")
    sp_lru.add_argument("--ops", type=int, default=64, help="随机写读操作次数")
    sp_lru.set_defaults(func=demo_lru)

    # viz group
    sp_viz = sub.add_parser("viz", help="算法/数据结构可视化")
    viz_sub = sp_viz.add_subparsers(dest="viz_cmd", required=True)

    # viz graph
    sp_vg = viz_sub.add_parser("graph", help="图算法可视化（BFS/DFS/拓扑 Kahn）")
    sp_vg.add_argument("--algo", choices=["bfs", "dfs", "topo", "topo_kahn"], default="bfs")
    sp_vg.add_argument("--directed", action="store_true", help="是否有向图（默认无向）")
    sp_vg.add_argument("--example", choices=["toy", "random"], default="toy", help="toy 示例或随机图")
    sp_vg.add_argument("--n", type=int, default=8, help="随机图节点数")
    sp_vg.add_argument("--p", type=float, default=0.25, help="随机图边概率")
    sp_vg.add_argument("--start", type=int, default=1, help="起点（bfs/dfs 使用）")
    sp_vg.add_argument("--fmt", choices=["png", "gif", "mp4", "pdf"], default="gif", help="输出格式")
    sp_vg.add_argument("--fps", type=int, default=2, help="动画帧率（gif/mp4 有效）")
    sp_vg.add_argument("--out", default="graph_viz.gif", help="输出文件路径")
    sp_vg.set_defaults(func=demo_viz_graph)

    # viz kmp
    sp_vk = viz_sub.add_parser("kmp", help="KMP 字符串匹配可视化")
    sp_vk.add_argument("--text", required=True, help="文本串")
    sp_vk.add_argument("--pattern", required=True, help="模式串")
    sp_vk.add_argument("--fmt", choices=["png", "gif", "mp4", "pdf"], default="gif")
    sp_vk.add_argument("--fps", type=int, default=2)
    sp_vk.add_argument("--out", default="kmp_viz.gif")
    sp_vk.set_defaults(func=demo_viz_kmp)

    # viz tree
    sp_vt = viz_sub.add_parser("tree", help="树结构插入可视化（BST/AVL/RBT/Treap）")
    sp_vt.add_argument("--kind", required=True, choices=["bst", "avl", "rbt", "rbtree", "treap"])
    sp_vt.add_argument("--seq", default="", help="逗号分隔的整数序列。为空则随机生成")
    sp_vt.add_argument("--n", type=int, default=12, help="随机序列长度")
    sp_vt.add_argument("--range", nargs=2, type=int, default=(1, 99), metavar=("LOW", "HIGH"), help="随机数范围 [LOW, HIGH]")
    sp_vt.add_argument("--fmt", choices=["png", "gif", "mp4", "pdf"], default="gif")
    sp_vt.add_argument("--fps", type=int, default=2)
    sp_vt.add_argument("--out", default="tree_viz.gif")
    sp_vt.set_defaults(func=demo_viz_tree)

    return p


def main(argv: Optional[Sequence[str]] = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
