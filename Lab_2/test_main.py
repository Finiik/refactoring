import unittest
import numpy as np
import os
from original import (
    function, compute_factorial, compute_combination, 
    delta_f, factorial_polynomial, approximate_function, 
    calculate_error, tabulate_original_function, parse_tabulation_line, 
    read_tabulated_data
)


class TestMathFunctions(unittest.TestCase):
    """Тести для математичних функцій"""

    def test_function(self):
        """Перевірка function(x) = cos(x^2)"""
        self.assertAlmostEqual(function(0), 1.0)  # cos(0) = 1
        self.assertAlmostEqual(function(np.pi / 2), np.cos((np.pi / 2) ** 2))
        self.assertAlmostEqual(function(1), np.cos(1**2))

    def test_compute_factorial(self):
        """Перевірка факторіалу"""
        self.assertEqual(compute_factorial(0), 1)
        self.assertEqual(compute_factorial(5), 120)
        self.assertEqual(compute_factorial(7), 5040)

    def test_compute_combination(self):
        """Перевірка біноміальних коефіцієнтів"""
        self.assertEqual(compute_combination(5, 2), 10)  # C(5,2) = 10
        self.assertEqual(compute_combination(6, 3), 20)
        self.assertEqual(compute_combination(7, 0), 1)

    def test_delta_f(self):
        """Перевірка обчислення скінченних різниць"""
        f_values = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(delta_f(0, f_values), 1)  # Має бути f[0]
        self.assertAlmostEqual(delta_f(1, f_values), 1)  # Має бути f[1] - f[0]
        self.assertAlmostEqual(delta_f(2, f_values), 0)  # Друга різниця повинна бути 0

    def test_factorial_polynomial(self):
        """Перевірка факторіального полінома"""
        self.assertAlmostEqual(factorial_polynomial(2, 2), 2)
        self.assertAlmostEqual(factorial_polynomial(3, 3), 6)
        self.assertAlmostEqual(factorial_polynomial(4, 2), 12)

    def test_approximate_function(self):
        """Перевірка апроксимації"""
        f_values = [function(x) for x in range(5)]
        approx_value = approximate_function(3, 1.5, f_values)
        exact_value = function(1.5)
        self.assertAlmostEqual(approx_value, exact_value, delta=0.1)

    def test_calculate_error(self):
        """Перевірка обчислення похибки"""
        self.assertAlmostEqual(calculate_error(5.0, 5.0), 0.0)
        self.assertAlmostEqual(calculate_error(10.0, 7.5), 2.5)
        self.assertAlmostEqual(calculate_error(0.0, 0.1), 0.1)

    def test_tabulate_original_function(self):
        """Перевірка запису табличних значень у файл"""
        file_name = "test_in.txt"
        tabulate_original_function(0, 2, 2, file_name)

        with open(file_name, "r") as file:
            lines = file.readlines()

        self.assertEqual(len(lines), 3)  # Має бути 3 рядки (0, 1, 2)
        self.assertTrue(lines[0].startswith("x=0.0"))
        self.assertTrue(lines[-1].startswith("x=2.0"))

        os.remove(file_name)

    def test_parse_tabulation_line(self):
        """Перевірка розбору рядка"""
        line = "x=3.14, y=0.999"
        x, y = parse_tabulation_line(line)
        self.assertAlmostEqual(x, 3.14)
        self.assertAlmostEqual(y, 0.999)

    def test_read_tabulated_data(self):
        """Перевірка зчитування табличних значень"""
        file_name = "test_in.txt"
        tabulate_original_function(0, 2, 2, file_name)
        data = read_tabulated_data(file_name)

        self.assertEqual(len(data), 3)
        self.assertAlmostEqual(data[0][0], 0.0)
        self.assertAlmostEqual(data[-1][0], 2.0)

        os.remove(file_name)


if __name__ == "__main__":
    unittest.original()
