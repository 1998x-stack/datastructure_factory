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
