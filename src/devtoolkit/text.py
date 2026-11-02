"""String helpers: URL-safe slugs and safe truncation."""

from __future__ import annotations

import re
import unicodedata

__all__ = ["slugify", "truncate"]

_SLUG_STRIP = re.compile(r"[^\w\s-]")
_SLUG_SPACES = re.compile(r"[-\s]+")


def slugify(value: str, separator: str = "-", max_length: int | None = None) -> str:
    """Convert ``value`` into a lowercase, URL-friendly slug.

    >>> slugify("Hello, World! 2024")
    'hello-world-2024'
    >>> slugify("  Multiple   spaces  ")
    'multiple-spaces'
    >>> slugify("A very long title", max_length=10)
    'a-very-lon'
    """
    if not isinstance(value, str):
        raise TypeError(f"slugify() expects str, got {type(value).__name__}")

    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    cleaned = _SLUG_STRIP.sub("", ascii_text).strip().lower()
    slug = _SLUG_SPACES.sub(separator, cleaned)

    if max_length is not None:
        if max_length < 0:
            raise ValueError("max_length must be >= 0")
        slug = slug[:max_length].rstrip(separator)

    return slug


def truncate(value: str, limit: int, suffix: str = "...") -> str:
    """Shorten ``value`` to ``limit`` characters, appending ``suffix`` when cut.

    The returned string is never longer than ``limit`` characters.

    >>> truncate("a very long sentence", 10)
    'a very...'
    >>> truncate("short", 10)
    'short'
    """
    if not isinstance(value, str):
        raise TypeError(f"truncate() expects str, got {type(value).__name__}")
    if limit < 0:
        raise ValueError("limit must be >= 0")

    if len(value) <= limit:
        return value

    if limit <= len(suffix):
        return value[:limit]

    return value[: limit - len(suffix)].rstrip() + suffix
