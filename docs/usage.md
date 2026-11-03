# Usage

Longer worked examples for each helper. The API is small on purpose, so
everything here fits on one screen.

## Text helpers

### `slugify(value, separator="-", max_length=None)`

Turns a title into something safe to put in a URL.

```python
from devtoolkit import slugify

slugify("Hello World!")                 # "hello-world"
slugify("  Multiple   spaces  ")        # "multiple-spaces"
slugify("Cafe\u0301 latté")             # "cafe-latte"
slugify("Hello World", separator="_")    # "hello_world"
slugify("A very long title", max_length=10)  # "a-very-lon"
```

Unicode accents are folded to ASCII, punctuation is dropped and runs of
whitespace collapse into the separator. `max_length` trims the result and
removes a trailing separator so you never end up with `hello-`.

### `truncate(value, limit, suffix="...")`

Shortens a string and marks that it was cut.

```python
from devtoolkit import truncate

truncate("a very long sentence", 10)          # "a very..."
truncate("short", 10)                         # "short"
truncate("a very long sentence", 10, suffix="~")  # "a very lo~"
```

The result is never longer than `limit`. When `limit` is smaller than the
suffix the raw prefix is returned instead.

## Batching helpers

### `chunk_list(items, size)`

Splits any iterable into consecutive lists.

```python
from devtoolkit import chunk_list

chunk_list([1, 2, 3, 4, 5], 2)   # [[1, 2], [3, 4], [5]]
chunk_list([], 3)                # []
chunk_list(range(5), 2)          # [[0, 1], [2, 3], [4]]
```

### `chunked(items, size)`

The lazy version. It yields chunks as it goes, so a generator or a very long
sequence is never held in memory all at once.

```python
from devtoolkit import chunked

for batch in chunked(range(1_000_000), 1000):
    process(batch)
```

## Environment helpers

```python
from devtoolkit import get_bool_env, get_env, get_float_env, get_int_env

get_env("PORT", "8080")        # "8080" when PORT is unset or empty
get_bool_env("CI")             # True for 1/true/yes/on in any case
get_int_env("WORKERS")         # int, raises ValueError on garbage
get_float_env("TIMEOUT", 2.5)  # float, raises ValueError on garbage
```

## Command line

```bash
devtoolkit --version
devtoolkit slugify "Hello World!"
devtoolkit truncate "a very long sentence" -l 10
devtoolkit chunk 5 2
```

The CLI mirrors the library one to one, so anything you can do in Python you
can do from a shell.
