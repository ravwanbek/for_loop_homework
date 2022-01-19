def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    odd_sum=0
    for x in range(N):
        if x%2!=0:
            odd_sum+=x


    return odd_sum
print(main(10))