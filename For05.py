def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    list=[]
    for x in range(A,B+1):
        list.append(x)
    a=list[::-1]
    return a
print(main(4,10))