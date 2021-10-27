import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculation(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_div_calculation(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtracion_calculation(self):
        assert self.calc.subtraction(self, 14, 5) == 9

    def test_add_calculation(self):
        assert self.calc.adding(self, 4, 9) == 13