import Rhino.Geometry as rg

def end_points_standard(x):
    """
    End Points (Standard)
    
    Args:
        x (Curve): Curve
    
    Retruns:
        (Tuple[Point3d, Point3d])
        - Start point of curve x.
        - End point of curve x.
    """
    
    # your code here
    if isinstance(x, rg.Polyline):
        return x[0], x[-1]
    elif isinstance(x, rg.Curve):
        return x.PointAtStart, x.PointAtEnd
    else:
        return None, None

a, b = end_points_standard(x)
