'''
def func(x):
    return x + 1

def test_func():
    assert func(3) == 5
'''

import sys

import pytest

sys.path.append('..')
print(sys.path)

from pythoncode.Calculator import Calculator


class TestCalculator():
    @pytest.mark.add
    def test_add(self):
        calc = Calculator()
        assert 2 == calc.add(1,1)

    @pytest.mark.add
    def test_add1(self):
        calc = Calculator()
        assert 4 == calc.add(2, 2)

    @pytest.mark.div
    def test_div(self):
        pass

    @pytest.mark.div
    def test_div1(self):
        pass
