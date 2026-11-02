"""Helpers for working with sequences in fixed-size batches."""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import TypeVar

__all__ = ["chunk_list", "chunked"]

T = TypeVar("T")


def chunk_list(items: Iterable[T], size: int) -> list[list[T]]:
    """Split ``items`` into consecutive lists of at most ``size`` elements.

    The final chunk holds the remainder and may be shorter than ``size``.
    The input is materialised, so it can be any iterable.

    >>> chunk_list([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    >>> chunk_list([], 3)
    []
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError(f"size must be an int, got {type(size).__name__}")
    if size <= 0:
        raise ValueError("size must be greater than 0")

    materialized = list(items)
    return [materialized[i : i + size] for i in range(0, len(materialized), size)]


def chunked(items: Iterable[T], size: int) -> Iterator[list[T]]:
    """Lazily yield consecutive chunks of at most ``size`` elements.

    Unlike :func:`chunk_list` this does not materialise the whole input, so it
    works with generators and very long sequences.

    >>> list(chunked(range(5), 2))
    [[0, 1], [2, 3], [4]]
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError(f"size must be an int, got {type(size).__name__}")
    if size <= 0:
        raise ValueError("size must be greater than 0")

    chunk: list[T] = []
    for item in items:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk
