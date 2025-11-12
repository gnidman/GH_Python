def delete_consecutive_standard(x, y):
    """
    Delete Consecutive (Standard)

    Args:
        x (List[Any]): List to process.
        y (bool): Wrap list.

    Returns:
        (List[Any], int)
        - New list with consecutive same items removed.
        - Number of removed items.
    """

    if not x:
        return [], 0

    result = [x[0]]
    for i in range(1, len(x)):
        if x[i] != x[i - 1]:
            result.append(x[i])


    if y and result and result[0] == result[-1]:
        result.pop()

    removed_number = len(x) - len(result)
    return result, removed_number
    

a, b = delete_consecutive_standard(x, y)
