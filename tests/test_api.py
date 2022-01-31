import pytest


class TestAPI:
    def test_init(self, app):
        assert app
