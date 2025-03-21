import numpy as np
import matplotlib.pyplot as plt
from approximator import FunctionApproximator
from tabulated_data import TabulatedData
from utils import function, calculate_error, save_results_to_file

# Константи
A, B = 0, 20  # Межі табуляції
N_VALUES = [5, 10, 20]  # Значення n

def plot_approximation_and_error(x_vals, original_func, approx_func, err_vals, n):
    """Будує графік апроксимації та похибки."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    ax1.plot(x_vals, original_func, label="Original Function")
    ax1.plot(x_vals, approx_func, label="Approximated Function", linestyle='--')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title(f'Function Approximation (n={n})')
    ax1.legend()
    ax1.grid(True)

    ax2.plot(x_vals, err_vals, label="Error", color='red')
    ax2.set_xlabel('x')
    ax2.set_ylabel('Error')
    ax2.set_title(f'Approximation Error (n={n})')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

def main():
    for n in N_VALUES:
        # 1. Табулюємо функцію та зчитуємо значення
        data = TabulatedData()
        data.tabulate_function(function, A, B, n)
        data.read_from_file()

        x_values = [x for x, _ in data.data]
        f_values = [y for _, y in data.data]

        # 2. Створюємо апроксиматор
        approximator = FunctionApproximator(n, f_values)
        
        # 3. Обчислюємо апроксимацію та похибку
        h = (B - A) / n
        total_pts = 20 * n
        t_values = np.linspace(0, n, total_pts + 1)
        
        approx_values, error_values, x_plot, func_values = [], [], [], []

        for t in t_values:
            appr = approximator.approximate(t)
            x_t = A + h * t
            exact = function(x_t)
            error = calculate_error(appr, exact)

            approx_values.append(appr)
            error_values.append(error)
            x_plot.append(x_t)
            func_values.append(exact)

        # 4. Записуємо результати у файли
        save_results_to_file("fappr.txt", t_values, approx_values)
        save_results_to_file("R.txt", t_values, error_values)

        # 5. Будуємо графіки
        plot_approximation_and_error(np.array(x_plot), np.array(func_values), np.array(approx_values), np.array(error_values), n)

if __name__ == "__main__":
    main()
