import pytest


pytest_plugins = "pytester"


@pytest.fixture
def tmp_tree_of_tests(pytester):
    """Create a temporary file test."""
    pytester.makepyfile(
        """
        def test_a1():
            assert False
        def test_a2():
            assert True
        def test_a3():
            assert True
        """)
    return pytester
