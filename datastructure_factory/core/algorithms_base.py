from typing import Protocol, Sequence, Any

class Sorter(Protocol):
    """排序算法协议（duck-typing）。"""

    def __call__(self, arr: Sequence[Any]) -> list[Any]:
        ...
