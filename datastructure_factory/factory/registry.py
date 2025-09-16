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
