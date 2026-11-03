"""devtoolkit - small dependency-free helpers for everyday developer scripting."""

__version__ = "0.3.0"
__all__ = [
    "__version__",
    "slugify",
    "truncate",
    "chunk_list",
    "chunked",
    "get_env",
    "get_bool_env",
    "get_int_env",
    "get_float_env",
]

_LAZY = {
    "slugify": "devtoolkit.text",
    "truncate": "devtoolkit.text",
    "chunk_list": "devtoolkit.collections",
    "chunked": "devtoolkit.collections",
    "get_env": "devtoolkit.env",
    "get_bool_env": "devtoolkit.env",
    "get_int_env": "devtoolkit.env",
    "get_float_env": "devtoolkit.env",
}


def __getattr__(name: str):
    # Lazy re-export keeps ``import devtoolkit`` cheap until a helper is used.
    module_name = _LAZY.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    import importlib

    return getattr(importlib.import_module(module_name), name)
