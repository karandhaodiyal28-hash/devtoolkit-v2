# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2026-11-03

### Added
- Environment variable helpers: `get_env`, `get_bool_env`, `get_int_env` and
  `get_float_env`. An empty string counts as unset, and numeric helpers raise a
  clear `ValueError` instead of failing later at the call site.
- `CONTRIBUTING.md` with the development setup and the guidelines for adding a
  helper.

## [0.2.0] - 2026-11-02

### Added
- `chunk_list()` - splits any iterable into consecutive lists of a fixed size.
- `chunked()` - lazy generator variant of the same idea.
- The `devtoolkit` command line interface with `slugify`, `truncate` and
  `chunk` subcommands.

## [0.1.0] - 2026-11-02

### Added
- `slugify()` - lowercase, URL-safe slugs with an optional separator and a
  maximum length.
- `truncate()` - shortens a string to a character limit and appends a suffix.
- CI workflow running the test suite on Python 3.9 to 3.12.

[Unreleased]: https://github.com/karandhaodiyal28-hash/devtoolkit/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/karandhaodiyal28-hash/devtoolkit/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/karandhaodiyal28-hash/devtoolkit/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/karandhaodiyal28-hash/devtoolkit/releases/tag/v0.1.0
