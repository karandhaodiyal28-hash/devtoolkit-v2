"""Environment variable helpers with defaults and light type coercion."""

from __future__ import annotations

import os

__all__ = ["get_env", "get_bool_env", "get_int_env", "get_float_env"]


def get_env(name: str, default: str | None = None) -> str | None:
    """Return the environment variable ``name``, or ``default`` when unset.

    An empty string is treated as unset, which matches how most config files
    behave.

    >>> get_env("HOME")
    '/home/karan'
    >>> get_env("NOT_SET_ANYWHERE", "fallback")
    'fallback'
    """
    value = os.environ.get(name)
    if value is None or value == "":
        return default
    return value


def get_bool_env(name: str, default: bool = False) -> bool:
    """Return a boolean environment variable.

    Accepts the usual truthy spellings: ``1``, ``true``, ``yes``, ``on``
    (case-insensitive). Anything else non-empty is treated as false.

    >>> get_bool_env("CI")
    True
    """
    value = os.environ.get(name)
    if value is None or value == "":
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def get_int_env(name: str, default: int | None = None) -> int | None:
    """Return an integer environment variable, or ``default`` if it is unset.

    Raises ``ValueError`` when the value is set but not a valid integer.

    >>> get_int_env("PORT")
    8080
    """
    raw = os.environ.get(name)
    if raw is None or raw == "":
        return default
    try:
        return int(raw)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer, got {raw!r}") from exc


def get_float_env(name: str, default: float | None = None) -> float | None:
    """Return a float environment variable, or ``default`` if it is unset.

    Raises ``ValueError`` when the value is set but not a valid float.

    >>> get_float_env("TIMEOUT")
    2.5
    """
    raw = os.environ.get(name)
    if raw is None or raw == "":
        return default
    try:
        return float(raw)
    except ValueError as exc:
        raise ValueError(f"{name} must be a number, got {raw!r}") from exc
