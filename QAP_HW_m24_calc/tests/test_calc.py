import pytest
from QAP_HW_m24_calc.app_calc.Calculator import Calculator

class TestCalc:
    def test_multiply_success(self):
        self.calc = Calculator
        assert self.calc.multiply(self, 9, 10) == 90

    def test_division_success(self):
        self.calc = Calculator
        assert self.calc.division(self, 33, 3) == 11

    def test_substraction_success(self):
        self.calc = Calculator
        assert self.calc.subtraction(self, 101, 51) == 50

    def test_adding_success(self):
        self.calc = Calculator
        assert self.calc.adding(self, 12, 3) == 15

    def teardown(self):
        print('Выполнение метода "teardown"')




