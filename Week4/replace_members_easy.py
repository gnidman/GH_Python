def replace_members_easy(x, y, z):
    """
    Replace Members (Easy)
    
    Args:
        x (List[int]): List to process.
        y (List[int]): Item(s) to replace.
        z (List[int]): Item(s) to replace with.
    
    Retruns:
        (List[int])
        All the items in x which are equal to items in y are replaced with items in z.
        
    """
    # your code here
    target = z[0]
    
    return [target if i in y else i for i in x]

a = replace_members_easy(x, y, z)