class main:
    # Python code
    
    # Read input
    x1, y1, x2, y2 = map(int, input().split())
    
    # Calculate x3, y3, x4, y4
    x3 = x2 + (y1 - y2)
    y3 = y2 - (x1 - x2)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    
    # Print output
    print(x3, y3, x4, y4)