import pytest

from devtoolkit.text import slugify, truncate


class TestSlugify:
    def test_basic(self):
        assert slugify("Hello World") == "hello-world"

    def test_strips_punctuation(self):
        assert slugify("Hello, World! 2024") == "hello-world-2024"

    def test_collapses_whitespace(self):
        assert slugify("  Multiple   spaces  ") == "multiple-spaces"

    def test_custom_separator(self):
        assert slugify("Hello World", separator="_") == "hello_world"

    def test_max_length(self):
        assert slugify("A very long title", max_length=10) == "a-very-lon"

    def test_empty_string(self):
        assert slugify("") == ""

    def test_non_string_raises(self):
        with pytest.raises(TypeError):
            slugify(123)


class TestTruncate:
    def test_shortens_with_suffix(self):
        assert truncate("a very long sentence", 10) == "a very..."

    def test_leaves_short_values_untouched(self):
        assert truncate("short", 10) == "short"

    def test_result_never_exceeds_limit(self):
        assert len(truncate("a very long sentence", 10)) <= 10

    def test_custom_suffix(self):
        assert truncate("a very long sentence", 10, suffix="~") == "a very lo~"

    def test_limit_smaller_than_suffix(self):
        assert truncate("a very long sentence", 2, suffix="...") == "a "

    def test_zero_limit(self):
        assert truncate("a very long sentence", 0) == ""

    def test_negative_limit_raises(self):
        with pytest.raises(ValueError):
            truncate("abc", -1)

    def test_non_string_raises(self):
        with pytest.raises(TypeError):
            truncate(None)
