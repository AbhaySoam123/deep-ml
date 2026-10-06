def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Your code here
    derivative = n*c*x**(n-1)
    return derivative