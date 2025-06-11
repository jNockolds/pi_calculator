import numpy as np

def measure_accuracy(approx_num):
    """
    Measure the number of digits (after 3) an approximation remains true against pi (with floating point precision).
    
    Parameters:
    approx (float): The approximated value.
    Returns:
    int: The number of correct digits in the approximation.
    """
    if approx_num == np.pi:
        return float('inf') # Infinite accuracy if the error is zero
    
    error = abs(approx_num - np.pi)
    
    return int(np.floor(-np.log10(error))) # Calculate the number of matching decimal places

assert(measure_accuracy(3.14157) == 4)