"""devtoolkit - small dependency-free helpers for everyday developer scripting."""

__version__ = "0.1.0"
__all__ = ["__version__", "slugify", "truncate"]


def __getattr__(name: str):
    # Lazy re-export keeps ``import devtoolkit`` cheap until a helper is used.
    if name in {"slugify", "truncate"}:
        from .text import slugify, truncate

        return {"slugify": slugify, "truncate": truncate}[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
