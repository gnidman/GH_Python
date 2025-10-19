import math

def round_standard(x):
    """
    Round (Standard)
    
    Args:
        x (float): Input value
    
    Retruns:
        (Tuple[int, int, int])
        - Neareast integer to x.
        - Floor value of x.
        - Ceiling value of x.
    """
    
    # your code here
    N = round(x)
    F = math.floor(x)
    C = math.ceil(x)

    return N, F, C

a, b, c = round_standard(x)