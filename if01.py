def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a > b:
        if b > c:        
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
           return c 
print(main(1, 4, 2))
print(main(-5, -3, -1))