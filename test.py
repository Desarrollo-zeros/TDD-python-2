import pytest
from main import *


def test_isprime():
    assert is_prime(2) == True


def test_fibonacci():
    assert fibonacci(1) == 1
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34