def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    x=''
    for b in range(n-1):
        x+=f'{b}'+','
    y=x+str(n-1)
        
    
    return y
        
        


    
print(main(3))