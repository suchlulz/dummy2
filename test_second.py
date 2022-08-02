from second import stuff
import pytest


def test_stuff():
    with pytest.raises(Exception):
        stuff()
