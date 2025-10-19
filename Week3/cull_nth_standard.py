def cull_nth_standard(x, y):
    """
    Cull nth (Standard)
    
    Args:
        x (List[Any]): List to cull.
        y (int): Cull yth.
    
    Retruns:
        (List[Any])
        Culled list.
        
    """
    # your code here
    for i in range(len(x), 0, -1):
        if i % y == 0:
            del x[i-1]

    return x

a = cull_nth_standard(x, y)