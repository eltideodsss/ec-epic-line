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

if __name__ == "__main__":
    num_to_factorize = 120
    factors = prime_factorization(num_to_factorize)
    print(f"Prime factors of {num_to_factorize}: {factors}")
    
    a = 1
    b = -3
    c = 2
    quadratic_solutions = solve_quadratic_equation(a, b, c)
    print(f"Solutions to the quadratic equation {a}x^2 + {b}x + {c} = 0: {quadratic_solutions}")
