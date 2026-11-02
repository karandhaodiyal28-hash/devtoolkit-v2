import pytest

from devtoolkit.collections import chunk_list, chunked


class TestChunkList:
    def test_even_split(self):
        assert chunk_list([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

    def test_remainder_chunk(self):
        assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

    def test_empty_input(self):
        assert chunk_list([], 3) == []

    def test_size_larger_than_input(self):
        assert chunk_list([1, 2], 10) == [[1, 2]]

    def test_accepts_generator(self):
        assert chunk_list(range(5), 2) == [[0, 1], [2, 3], [4]]

    def test_zero_size_raises(self):
        with pytest.raises(ValueError):
            chunk_list([1, 2], 0)

    def test_negative_size_raises(self):
        with pytest.raises(ValueError):
            chunk_list([1, 2], -1)

    def test_non_int_size_raises(self):
        with pytest.raises(TypeError):
            chunk_list([1, 2], "2")


class TestChunked:
    def test_lazy_generator(self):
        result = chunked(range(5), 2)
        assert not isinstance(result, list)
        assert list(result) == [[0, 1], [2, 3], [4]]

    def test_exact_multiple(self):
        assert list(chunked(range(4), 2)) == [[0, 1], [2, 3]]

    def test_empty_input(self):
        assert list(chunked([], 2)) == []

    def test_consumes_generator_input(self):
        def source():
            yield from (1, 2, 3)

        assert list(chunked(source(), 2)) == [[1, 2], [3]]

    def test_zero_size_raises(self):
        with pytest.raises(ValueError):
            list(chunked([1], 0))
