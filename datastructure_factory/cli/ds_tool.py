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
