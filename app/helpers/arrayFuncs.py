from typing import Iterable, Callable, TypeVar

_T = TypeVar("_T")


def arrFind(arr: Iterable[_T], func: Callable, default: _T = None) -> _T | None:
    return next(filter(func, arr), default)


def arrGet(arr: Iterable[_T], index: int, default: _T = None) -> _T | None:
    return arr[index] if len(arr) > index else default
