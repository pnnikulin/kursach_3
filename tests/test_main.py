import pytest

from src import main


def test_main():
    assert main() == None

if __name__ == "__main__":
    pytest.main()