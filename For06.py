def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    list_sum=0
    for x in range(A,B):
        list_sum+=x 

    return list_sum
print(main(1,5))