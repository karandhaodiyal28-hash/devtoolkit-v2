import hashlib

import pytest

from devtoolkit.hashing import checksum, file_checksum, sha256_bytes


class TestChecksum:
    def test_sha256_of_abc(self):
        assert checksum(b"abc") == (
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
        )

    def test_md5_of_abc(self):
        assert checksum(b"abc", "md5") == "900150983cd24fb0d6963f7d28e17f72"

    def test_empty_input(self):
        assert checksum(b"") == hashlib.sha256(b"").hexdigest()

    def test_accepts_bytearray(self):
        assert checksum(bytearray(b"abc")) == checksum(b"abc")

    def test_unknown_algorithm_raises(self):
        with pytest.raises(ValueError, match="unknown hash algorithm"):
            checksum(b"abc", "not-a-real-algorithm")

    def test_non_bytes_raises(self):
        with pytest.raises(TypeError):
            checksum("abc")


class TestSha256Bytes:
    def test_matches_checksum(self):
        assert sha256_bytes(b"abc") == checksum(b"abc", "sha256")


class TestFileChecksum:
    def test_matches_bytes_checksum(self, tmp_path):
        target = tmp_path / "payload.bin"
        target.write_bytes(b"abc")

        assert file_checksum(target) == checksum(b"abc")

    def test_accepts_string_path(self, tmp_path):
        target = tmp_path / "payload.bin"
        target.write_bytes(b"abc")

        assert file_checksum(str(target)) == checksum(b"abc")

    def test_reads_in_chunks_for_large_files(self, tmp_path):
        target = tmp_path / "big.bin"
        target.write_bytes(b"x" * (200 * 1024))

        assert file_checksum(target) == checksum(b"x" * (200 * 1024))

    def test_missing_file_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            file_checksum(tmp_path / "nope.bin")

    def test_directory_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            file_checksum(tmp_path)
