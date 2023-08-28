import numpy as np
import sympy as sp

def prime_factorization(n):
    factors = []
    divisor = 2
    while n >= 2:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return factors

def solve_quadratic_equation(a, b, c):
    x = sp.symbols('x')
    equation = a * x**2 + b * x + c
    solutions = sp.solve(equation, x)
    return solutions

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def matrix_power(matrix, power):
    result = matrix.copy()
    for _ in range(power - 1):
        result = np.dot(result, matrix)
    return result

if __name__ == "__main__":
    num_to_factorize = 9876543210
    factors = prime_factorization(num_to_factorize)
    print(f"Prime factors of {num_to_factorize}: {factors}")
    
    a = 2
    b = -5
    c = 3
    quadratic_solutions = solve_quadratic_equation(a, b, c)
    print(f"Solutions to the quadratic equation {a}x^2 + {b}x + {c} = 0: {quadratic_solutions}")
    
    fibonacci_sequence = [fibonacci_recursive(i) for i in range(20)]
    print(f"Fibonacci sequence: {fibonacci_sequence}")
    
    matrix_size = 3
    random_matrix = np.random.randint(0, 10, size=(matrix_size, matrix_size))
    power = 5
    matrix_raised = matrix_power(random_matrix, power)
    print(f"Random Matrix:\n{random_matrix}")
    print(f"Matrix raised to power {power}:\n{matrix_raised}")
