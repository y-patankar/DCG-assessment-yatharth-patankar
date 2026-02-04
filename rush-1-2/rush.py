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
    # When height is 1
    if y==1:
        print("*" * x)
        return
    for row in range(y):
        # Top row
        if row == 0 :
            if x == 1:
                print("*")
            else:
                print("/" + "*" * (x - 2) + "\\")
        # Bottom row
        elif row == y-1:
            if x==1:
                print("*")
            else:
                print("\\" + "*" * (x - 2) + "/")
        # Middle Rows
        else:
            if x == 1:
                print("*")
            else:
                print("*" + " " * (x - 2) + "*")