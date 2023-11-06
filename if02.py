def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a < b:
        if b > c:        
            return a
        else:
            return c
    else:
        if a < b:
            return b
        else:
           return a
print(main(1, 4, 2))
print(main(-1, -3, -5))