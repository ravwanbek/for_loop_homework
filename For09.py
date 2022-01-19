def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    list=[]
    for x in range(1,11):
        list.append(x*price)

    return list
print(main(150))