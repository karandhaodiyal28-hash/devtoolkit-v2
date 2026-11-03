import hashlib

import pytest

from devtoolkit.cli import build_parser, main


class TestCli:
    def test_slugify(self, capsys):
        assert main(["slugify", "Hello World!"]) == 0
        assert capsys.readouterr().out.strip() == "hello-world"

    def test_slugify_with_separator(self, capsys):
        assert main(["slugify", "Hello World", "-s", "_"]) == 0
        assert capsys.readouterr().out.strip() == "hello_world"

    def test_slugify_with_max_length(self, capsys):
        assert main(["slugify", "A very long title", "-m", "6"]) == 0
        assert capsys.readouterr().out.strip() == "a-very"

    def test_truncate(self, capsys):
        assert main(["truncate", "a very long sentence", "-l", "10"]) == 0
        assert capsys.readouterr().out.strip() == "a very..."

    def test_truncate_custom_suffix(self, capsys):
        assert main(["truncate", "a very long sentence", "-l", "10", "--suffix", "~"]) == 0
        assert capsys.readouterr().out.strip() == "a very lo~"

    def test_chunk(self, capsys):
        assert main(["chunk", "5", "2"]) == 0
        assert capsys.readouterr().out.strip() == "0 1\n2 3\n4"

    def test_hash(self, capsys, tmp_path):
        target = tmp_path / "payload.bin"
        target.write_bytes(b"abc")

        assert main(["hash", str(target)]) == 0
        assert capsys.readouterr().out.strip() == hashlib.sha256(b"abc").hexdigest()

    def test_hash_with_algorithm(self, capsys, tmp_path):
        target = tmp_path / "payload.bin"
        target.write_bytes(b"abc")

        assert main(["hash", str(target), "-a", "md5"]) == 0
        assert capsys.readouterr().out.strip() == hashlib.md5(b"abc").hexdigest()

    def test_hash_missing_file_exits_non_zero(self, tmp_path):
        with pytest.raises(SystemExit) as exc:
            main(["hash", str(tmp_path / "nope.bin")])
        assert exc.value.code == 1

    def test_hash_unknown_algorithm_exits_non_zero(self, tmp_path):
        target = tmp_path / "payload.bin"
        target.write_bytes(b"abc")

        with pytest.raises(SystemExit) as exc:
            main(["hash", str(target), "-a", "not-real"])
        assert exc.value.code == 1

    def test_missing_command_errors(self):
        with pytest.raises(SystemExit):
            build_parser().parse_args([])

    def test_unknown_command_errors(self):
        with pytest.raises(SystemExit):
            main(["nope"])
