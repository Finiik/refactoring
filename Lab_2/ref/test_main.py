import unittest
import os
import numpy as np
from approximator import FunctionApproximator
from tabulated_data import TabulatedData
from utils import (
    function, compute_factorial, compute_combination, 
    delta_f, factorial_polynomial, calculate_error, 
    save_results_to_file
)

class TestMathFunctions(unittest.TestCase):
    """Тести для математичних функцій"""

    def test_factorial_edge_cases(self):
        """Перевірка факторіалу для граничних випадків"""
        self.assertEqual(compute_factorial(0), 1)  # 0! = 1
        self.assertEqual(compute_factorial(1), 1)  # 1! = 1
        self.assertEqual(compute_factorial(10), 3628800)  # 10! = 3628800

        # Тест на велике число (20! = 2.43 * 10^18)
        self.assertEqual(compute_factorial(20), 2432902008176640000)

        # Перевірка на негативні числа (повинен бути виняток)
        with self.assertRaises(ValueError):
            compute_factorial(-5)
        
    def test_function(self):
        """Перевірка function(x) = cos(x^2)"""
        self.assertAlmostEqual(function(0), 1.0)  # cos(0) = 1
        self.assertAlmostEqual(function(np.pi / 2), np.cos((np.pi / 2) ** 2))


    def test_compute_combination(self):
        """Перевірка біноміальних коефіцієнтів"""
        self.assertEqual(compute_combination(5, 2), 10)  # C(5,2) = 10
        self.assertEqual(compute_combination(6, 3), 20)
        self.assertEqual(compute_combination(7, 0), 1)

class TestTabulatedData(unittest.TestCase):
    """Тести для класу TabulatedData"""

    def setUp(self):
        """Створення тестових даних перед тестами"""
        self.file_name = "test_in.txt"
        self.tabulated_data = TabulatedData(self.file_name)

    def test_tabulate_function(self):
        """Перевірка табуляції функції"""
        self.tabulated_data.tabulate_function(function, 0, 2, 2)
        self.assertEqual(len(self.tabulated_data.data), 3)

    def test_write_and_read_from_file(self):
        """Перевірка запису та зчитування даних з файлу"""
        self.tabulated_data.tabulate_function(function, 0, 2, 2)
        self.tabulated_data.write_to_file()
        self.tabulated_data.read_from_file()

        self.assertEqual(len(self.tabulated_data.data), 3)
        self.assertAlmostEqual(self.tabulated_data.data[0][0], 0.0)
        self.assertAlmostEqual(self.tabulated_data.data[-1][0], 2.0)

    def tearDown(self):
        """Видалення тестового файлу після тестів"""
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

class TestFunctionApproximator(unittest.TestCase):
    """Тести для класу FunctionApproximator"""

    def setUp(self):
        """Налаштування тестових даних"""
        self.f_values = [function(x) for x in range(5)]
        self.approximator = FunctionApproximator(4, self.f_values)

    def test_approximate(self):
        """Перевірка апроксимації"""
        approx_value = self.approximator.approximate(2)
        exact_value = function(2)
        self.assertAlmostEqual(approx_value, exact_value, delta=0.1)

class TestHelperFunctions(unittest.TestCase):
    """Тести для допоміжних функцій"""

    def test_delta_f(self):
        """Перевірка обчислення скінченних різниць"""
        f_values = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(delta_f(0, f_values), 1)  
        self.assertAlmostEqual(delta_f(1, f_values), 1)  

    def test_factorial_polynomial(self):
        """Перевірка факторіального полінома"""
        self.assertAlmostEqual(factorial_polynomial(2, 2), 2)
        self.assertAlmostEqual(factorial_polynomial(3, 3), 6)
        self.assertAlmostEqual(factorial_polynomial(4, 2), 12)

    def test_calculate_error(self):
        """Перевірка обчислення похибки"""
        self.assertAlmostEqual(calculate_error(5.0, 5.0), 0.0)
        self.assertAlmostEqual(calculate_error(10.0, 7.5), 2.5)

class TestFileOperations(unittest.TestCase):
    """Тести для роботи з файлами"""

    def setUp(self):
        """Налаштування тестового файлу"""
        self.file_name = "test_results.txt"

    def test_save_results_to_file(self):
        """Перевірка запису у файл"""
        t_values = [0, 1, 2, 3]
        values = [0.1, 0.2, 0.3, 0.4]
        save_results_to_file(self.file_name, t_values, values)

        with open(self.file_name, "r") as file:
            lines = file.readlines()

        self.assertEqual(len(lines), 4)
        self.assertTrue(lines[0].startswith("0\t0.1"))

    def tearDown(self):
        """Видалення тестового файлу"""
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

if __name__ == "__main__":
    unittest.main()
