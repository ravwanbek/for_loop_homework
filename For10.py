def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    list=[]
    for x in list1:
        list.append(x.capitalize())



    return list
print(main(['ali','vali','gani']))