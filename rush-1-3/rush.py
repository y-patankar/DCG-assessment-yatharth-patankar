import sys

def rush(x,y):
    """
    Display a square pattern based on x (width) and y (height)
    Args:
    
    x (int): Width of the square
    y (int): Height of the square
    """
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return
    # Your implementation here
    if y==1:
        print("B" * x)
        return
    if x==1:
        for row in range(y):
            print("B")
        return
    for row in range(y):
        if row == 0:
            print("A" + "B" * (x - 2) + "A")
        elif row == y - 1:
            print("C" + "B" * (x - 2) + "C")
        else:
            print("B" + " " * (x - 2) + "B")
