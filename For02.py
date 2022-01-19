def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    a=list(range(n))
    for b in a:
        x=''.join(str(b) for b in a)
    
    return x
        
        


    
print(main(8))