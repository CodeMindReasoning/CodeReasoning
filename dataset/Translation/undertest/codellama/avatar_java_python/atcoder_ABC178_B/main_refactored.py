class main:
    import math
    
    a, b, c, d = map(int, input().split())
    
    print(max(max(max(a * c, b * d), a * d), b * c))