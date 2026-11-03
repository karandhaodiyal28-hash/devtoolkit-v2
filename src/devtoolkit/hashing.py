"""Checksum helpers for bytes, text and files."""

from __future__ import annotations

import hashlib
from pathlib import Path

__all__ = ["checksum", "sha256_bytes", "file_checksum"]

_CHUNK_SIZE = 64 * 1024


def checksum(data: bytes, algorithm: str = "sha256") -> str:
    """Return the hex digest of ``data`` using ``algorithm``.

    >>> checksum(b"abc")
    'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
    >>> checksum(b"abc", "md5")
    '900150983cd24fb0d6963f7d28e17f72'
    """
    if not isinstance(data, (bytes, bytearray, memoryview)):
        raise TypeError(f"checksum() expects bytes, got {type(data).__name__}")

    try:
        digest = hashlib.new(algorithm)
    except ValueError as exc:
        raise ValueError(f"unknown hash algorithm: {algorithm!r}") from exc

    digest.update(bytes(data))
    return digest.hexdigest()


def sha256_bytes(data: bytes) -> str:
    """Return the SHA-256 hex digest of ``data``.

    A named shortcut for :func:`checksum` when the algorithm is always the
    same, so call sites do not repeat the string.
    """
    return checksum(data, "sha256")


def file_checksum(path: str | Path, algorithm: str = "sha256") -> str:
    """Return the hex digest of the file at ``path``.

    The file is read in chunks, so hashing a multi-gigabyte file does not
    need that much memory.

    Raises ``FileNotFoundError`` when the path does not exist.
    """
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"not a file: {file_path}")

    try:
        digest = hashlib.new(algorithm)
    except ValueError as exc:
        raise ValueError(f"unknown hash algorithm: {algorithm!r}") from exc

    with file_path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(_CHUNK_SIZE), b""):
            digest.update(chunk)

    return digest.hexdigest()
