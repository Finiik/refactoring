from utils import delta_f, factorial_polynomial, compute_factorial

class FunctionApproximator:
    """Клас для апроксимації функції методом скінченних різниць."""
    def __init__(self, n, f_values):
        self.n = n
        self.f_values = f_values

    def approximate(self, t):
        """Обчислює апроксимацію функції в точці t."""
        result = sum(
            delta_f(k, self.f_values) * factorial_polynomial(t, k) / compute_factorial(k)
            for k in range(self.n + 1)
        )
        return result
