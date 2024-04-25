import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")
from main import *


@pytest.fixture()
def resource():
    print("setup")
    yield "ressourve"
    print("teardown")


def test_one():
    assert True is True
