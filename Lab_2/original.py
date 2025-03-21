import numpy as np
import matplotlib.pyplot as plt
from math import fabs, factorial, comb
from typing import List, Tuple


def function(x: float) -> float:
    return np.cos(x**2)


def compute_factorial(k: int) -> int:
    return factorial(k)


def compute_combination(n: int, k: int) -> int:
    return comb(n, k)


def step(n: int) -> int:
    return -1 if n % 2 else 1


def delta_f(n: int, f_values: List[float]) -> float:
    result = 0.0
    for k in range(n + 1):
        result += f_values[k] * step(n - k) * compute_combination(n, k)
    return result


def factorial_polynomial(t: float, k: int) -> float:
    product = 1.0
    if k == 0:
        product = 1
    else:
        for i in range(k):
            product *= (t - i)
    return product


def approximate_function(n: int, t: float, f_values: List[float]) -> float:
    result = 0.0
    for k in range(n + 1):
        delta = delta_f(k, f_values)
        term = delta * factorial_polynomial(t, k) / compute_factorial(k)
        result += term
    return result


def calculate_error(approx_value: float, exact_value: float) -> float:
    return fabs(approx_value - exact_value)


def tabulate_original_function(a: float, b: float, num_points: int, file_name='in.txt') -> None:
    h = (b - a) / num_points
    with open(file_name, 'w') as file:
        for i in range(num_points + 1):
            x = a + i * h
            y = function(x)
            file.write(f"x={x}, y={y}\n")


def parse_tabulation_line(line: str, separator=', ') -> Tuple[float, float]:
    splitted_line_values = line.rstrip('\n').split(separator)
    x = float(splitted_line_values[0].lstrip('x='))
    y = float(splitted_line_values[1].lstrip('y='))
    return (x, y)


def read_tabulated_data(file_name='in.txt') -> List[Tuple[float, float]]:
    values_from_file = []
    with open(file_name) as file:
        for line in file.readlines():
            values_from_file.append(parse_tabulation_line(line))
    return values_from_file


def plot_approximation_and_error(x_vals: np.ndarray, original_func: np.ndarray, approx_func: np.ndarray, err_vals: np.ndarray, n: int) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    ax1.plot(x_vals, original_func, label="Original Function")
    ax1.plot(x_vals, approx_func, label="Approximated Function", linestyle='--')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title(f'Function Approximation ({n=})')
    ax1.legend()
    ax1.grid(True)

    ax2.plot(x_vals, err_vals, label="Error", color='red')
    ax2.set_xlabel('x')
    ax2.set_ylabel('Error')
    ax2.set_title(f'Approximation Error ({n=})')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.show()


def main():
    n = [5, 10, 20]
    a = 0
    b = 20

    for n in n:
        num_points = n

        tabulate_original_function(a, b, num_points, 'in.txt')
        tabulated_data = read_tabulated_data('in.txt')
        x_values = [data[0] for data in tabulated_data]
        f_values = [data[1] for data in tabulated_data]

        h = (b - a) / n
        total_pts = 20 * n
        ht = n / total_pts

        t_values = np.linspace(0, n, total_pts + 1)
        approx_values = []
        error_values = []
        x_plot = []
        func_values = []

        for t in t_values:
            appr = approximate_function(n, t, f_values)
            x_t = a + h * t
            exact = function(x_t)
            error = calculate_error(appr, exact)
            approx_values.append(appr)
            error_values.append(error)
            x_plot.append(x_t)
            func_values.append(exact)

        with open('fappr.txt', 'w') as fappr_file:
            for t, appr in zip(t_values, approx_values):
                fappr_file.write(f"{t}\t{appr}\n")

        with open('R.txt', 'w') as error_file:
            for t, error in zip(t_values, error_values):
                error_file.write(f"{t}\t{error}\n")

        plot_approximation_and_error(np.array(x_plot), np.array(
            func_values), np.array(approx_values), np.array(error_values), n)


if __name__ == '__main__':
    main()