import pytest

from devtoolkit.env import get_bool_env, get_env, get_float_env, get_int_env


class TestGetEnv:
    def test_returns_value(self, monkeypatch):
        monkeypatch.setenv("DK_TEST", "value")
        assert get_env("DK_TEST") == "value"

    def test_default_when_unset(self, monkeypatch):
        monkeypatch.delenv("DK_TEST", raising=False)
        assert get_env("DK_TEST", "fallback") == "fallback"

    def test_empty_string_is_treated_as_unset(self, monkeypatch):
        monkeypatch.setenv("DK_TEST", "")
        assert get_env("DK_TEST", "fallback") == "fallback"

    def test_returns_none_without_default(self, monkeypatch):
        monkeypatch.delenv("DK_TEST", raising=False)
        assert get_env("DK_TEST") is None


class TestGetBoolEnv:
    @pytest.mark.parametrize("raw", ["1", "true", "TRUE", "yes", "on", "On"])
    def test_truthy_values(self, monkeypatch, raw):
        monkeypatch.setenv("DK_TEST", raw)
        assert get_bool_env("DK_TEST") is True

    @pytest.mark.parametrize("raw", ["0", "false", "no", "off", "maybe"])
    def test_falsy_values(self, monkeypatch, raw):
        monkeypatch.setenv("DK_TEST", raw)
        assert get_bool_env("DK_TEST") is False

    def test_default_when_unset(self, monkeypatch):
        monkeypatch.delenv("DK_TEST", raising=False)
        assert get_bool_env("DK_TEST", True) is True


class TestGetIntEnv:
    def test_parses_int(self, monkeypatch):
        monkeypatch.setenv("DK_TEST", "8080")
        assert get_int_env("DK_TEST") == 8080

    def test_default_when_unset(self, monkeypatch):
        monkeypatch.delenv("DK_TEST", raising=False)
        assert get_int_env("DK_TEST", 80) == 80

    def test_invalid_value_raises(self, monkeypatch):
        monkeypatch.setenv("DK_TEST", "not-a-number")
        with pytest.raises(ValueError, match="must be an integer"):
            get_int_env("DK_TEST")


class TestGetFloatEnv:
    def test_parses_float(self, monkeypatch):
        monkeypatch.setenv("DK_TEST", "2.5")
        assert get_float_env("DK_TEST") == 2.5

    def test_default_when_unset(self, monkeypatch):
        monkeypatch.delenv("DK_TEST", raising=False)
        assert get_float_env("DK_TEST", 1.0) == 1.0

    def test_invalid_value_raises(self, monkeypatch):
        monkeypatch.setenv("DK_TEST", "abc")
        with pytest.raises(ValueError, match="must be a number"):
            get_float_env("DK_TEST")
