import Rhino.Geometry as rg
def box_2pt_easy(x, y):
    """
    Box 2Pt (Easy)
    
    Args:
        x (Point3D): First corner.
        y (Point3D): Second corner.
    
    Retruns:
        (Box)
        Box with corner x, y, created in World XY.
    """
    # your code here

    min_x = min(x.X, y.X)
    max_x = max(x.X, y.X)
    min_y = min(x.Y, y.Y)
    max_y = max(x.Y, y.Y)
    min_z = min(x.Z, y.Z)
    max_z = max(x.Z, y.Z)
    
    origin_pt = rg.Point3d(min_x, min_y, min_z)
    
    z_vector = rg.Vector3d(0,0,1)
    plane_xy = rg.Plane(origin_pt, z_vector)
    
    x_size = rg.Interval(0, max_x - min_x)
    y_size = rg.Interval(0, max_y - min_y)
    z_size = rg.Interval(0, max_z - min_z)
    
    a = rg.Box(plane_xy, x_size, y_size, z_size)
    
    return a

a = box_2pt_easy(x, y)