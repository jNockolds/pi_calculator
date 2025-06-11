import numpy as np
from random import random


def monte_carlo(iterations : int) -> float:
    """
    Estimate the value of pi using the Monte Carlo method.
    This function generates a list of random points in a unit square and counts how many fall within a quarter circle.
    Args:
        n (int): The number of random points to generate.
    Returns:
        float: The estimated value of pi.
    """
    x = np.random.random(iterations)
    y = np.random.random(iterations)
    return np.sum(x**2 + y**2 <= 1) * 4 / iterations


def leibniz_formula(iterations : int) -> float:
    """
    Estimate the value of pi using the Leibniz formula.
    The Leibniz formula for π is given by:
    π = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)
    Args:
        iterations (int): The number of terms to include in the series.
    Returns:
        float: The estimated value of pi.
    """
    sum = 0.0
    for i in range(0, iterations // 2, 2):
        sum += 4 / (2 * i + 1)
    for i in range(1, iterations // 2, 2):
        sum += - 4 / (2 * i + 1)
    return sum
