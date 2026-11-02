"""Command line interface for devtoolkit."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from .collections import chunk_list
from .text import slugify, truncate

__all__ = ["main", "build_parser"]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="devtoolkit",
        description="Small helpers for everyday developer scripting.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    slug_cmd = sub.add_parser("slugify", help="Convert text into a URL-safe slug.")
    slug_cmd.add_argument("text", help="Text to convert.")
    slug_cmd.add_argument("-s", "--separator", default="-", help="Separator (default: -).")
    slug_cmd.add_argument("-m", "--max-length", type=int, default=None, help="Trim the slug.")

    trunc_cmd = sub.add_parser("truncate", help="Shorten text to a character limit.")
    trunc_cmd.add_argument("text", help="Text to shorten.")
    trunc_cmd.add_argument("-l", "--limit", type=int, required=True, help="Max characters.")
    trunc_cmd.add_argument("--suffix", default="...", help="Suffix when cut (default: ...).")

    chunk_cmd = sub.add_parser("chunk", help="Split a range into fixed size chunks.")
    chunk_cmd.add_argument("count", type=int, help="Number of items.")
    chunk_cmd.add_argument("size", type=int, help="Chunk size.")

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "slugify":
        print(slugify(args.text, separator=args.separator, max_length=args.max_length))
        return 0

    if args.command == "truncate":
        print(truncate(args.text, args.limit, suffix=args.suffix))
        return 0

    if args.command == "chunk":
        for chunk in chunk_list(range(args.count), args.size):
            print(" ".join(str(item) for item in chunk))
        return 0

    parser.error(f"unknown command: {args.command}")
    return 2


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
