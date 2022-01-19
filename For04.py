def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    list=[]
    for x in range(A,B+1):
        list.append(x) 

    return list
print(main(2,9))