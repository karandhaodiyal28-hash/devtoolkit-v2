# devtoolkit

Small, dependency-free helpers for the kind of thing you end up rewriting in every
project.

## Install

```bash
pip install -e .
```

## Usage

```python
from devtoolkit import slugify, truncate

slugify("Hello World!")             # -> "hello-world"
truncate("a very long sentence", 10) # -> "a very..."
```

## Development

```bash
python -m pip install -e .
python -m pytest tests -q
```

## License

MIT - see [LICENSE](LICENSE).
