import numpy as np
from math import factorial, comb, fabs

def function(x):
    """Цільова функція."""
    return np.cos(x**2)

def compute_factorial(k):
    """Обчислює факторіал."""
    return factorial(k)

def compute_combination(n, k):
    """Обчислює біноміальний коефіцієнт."""
    return comb(n, k)

def step(n):
    """Повертає (-1)^n."""
    return -1 if n % 2 else 1

def delta_f(n, f_values):
    """Обчислює скінченні різниці."""
    return sum(f_values[k] * step(n - k) * compute_combination(n, k) for k in range(n + 1))

def factorial_polynomial(t, k):
    """Обчислює факторіальний поліном."""
    product = 1.0
    for i in range(k):
        product *= (t - i)
    return product

def calculate_error(approx_value, exact_value):
    """Обчислює похибку."""
    return fabs(approx_value - exact_value)

def save_results_to_file(file_name, t_values, values):
    """Записує результати у файл."""
    with open(file_name, 'w') as file:
        for t, value in zip(t_values, values):
            file.write(f"{t}\t{value}\n")
