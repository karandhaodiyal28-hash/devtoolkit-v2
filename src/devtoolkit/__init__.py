"""devtoolkit - small dependency-free helpers for everyday developer scripting."""

__version__ = "0.2.0"
__all__ = ["__version__", "slugify", "truncate", "chunk_list", "chunked"]

_LAZY = {
    "slugify": "devtoolkit.text",
    "truncate": "devtoolkit.text",
    "chunk_list": "devtoolkit.collections",
    "chunked": "devtoolkit.collections",
}


def __getattr__(name: str):
    # Lazy re-export keeps ``import devtoolkit`` cheap until a helper is used.
    module_name = _LAZY.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    import importlib

    return getattr(importlib.import_module(module_name), name)
