# devtoolkit

Small, dependency-free helpers for the kind of thing you end up rewriting in every
project.

## Install

```bash
pip install -e .
```

## Usage

```python
from devtoolkit import chunk_list, chunked, checksum, get_bool_env, get_env, slugify, truncate

slugify("Hello World!")             # -> "hello-world"
truncate("a very long sentence", 10) # -> "a very..."
chunk_list([1, 2, 3, 4, 5], 2)      # -> [[1, 2], [3, 4], [5]]
list(chunked(range(5), 2))          # -> [[0, 1], [2, 3], [4]]
get_env("PORT", "8080")             # -> "8080"
get_bool_env("CI")                  # -> True
checksum(b"abc")                    # -> sha256 hex digest
```

`chunked()` is the lazy variant - it never holds the whole input in memory.
`get_env()` and friends treat an empty string as unset and raise a clear
`ValueError` when a numeric variable holds something that is not a number.

## CLI

```bash
devtoolkit slugify "Hello World!"        # hello-world
devtoolkit truncate "a very long..." -l 10 # a very...
devtoolkit chunk 5 2                      # 0 1 / 2 3 / 4
```

## Development

```bash
python -m pip install -e .
python -m pytest tests -q
```

## License

MIT - see [LICENSE](LICENSE).
