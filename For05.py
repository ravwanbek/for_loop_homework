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
    for x in range(B,A+1):
        list.append(x)
    return list
print(main(10,4))