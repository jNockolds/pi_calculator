from numpy import pi
from utils import measure_accuracy
from pi_estimations import *

iterations = 1000000 # Number of random points generated for the Monte Carlo simulation

algorithms = [monte_carlo, leibniz_formula]
algorithm = algorithms[1]

pi_estimate = algorithm(iterations)
print(f"Estimated value of pi (π) after {iterations} iterations: {pi_estimate} (error: {100 * abs(pi - pi_estimate) / pi}%)")
print("                                      Actual value:", pi)
