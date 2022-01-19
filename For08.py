def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    calc=0
    
    for x in range(1,N+1):
        calc+=(1/x)

    return calc
print(main(4))