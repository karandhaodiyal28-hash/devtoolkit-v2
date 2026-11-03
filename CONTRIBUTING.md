# Contributing to devtoolkit

Thanks for taking the time to help. This is a small, dependency-free helper
library, so the bar for a change is low but the expectations are clear.

## Getting set up

```bash
git clone https://github.com/karandhaodiyal28-hash/devtoolkit.git
cd devtoolkit
python -m pip install -e .
python -m pip install pytest
```

## Running the tests

```bash
python -m pytest tests -q
```

Every pull request should keep the suite green. CI runs it on Python 3.9, 3.10,
3.11 and 3.12.

## Guidelines

- Keep the library dependency-free. A new runtime dependency needs a strong
  reason.
- Public helpers get a docstring with a doctest example, and a matching test.
- Keep the CLI surface small; prefer adding a subcommand over adding flags to
  an existing one.
- Write commit messages in the conventional style used in the history:
  `feat(scope): ...`, `fix(scope): ...`, `chore: ...`.

## Adding a helper

1. Put it in the module that matches its kind (`text.py`, `collections.py`,
   `env.py`).
2. Re-export it lazily from `devtoolkit/__init__.py`.
3. Add tests covering the happy path, the edges and the error cases.
4. Add a line to `CHANGELOG.md` under the unreleased section.

## Releasing

Version tags are pushed as `vX.Y.Z`. The publish workflow runs the test suite,
builds the distributions and releases them to PyPI using trusted publishing.
