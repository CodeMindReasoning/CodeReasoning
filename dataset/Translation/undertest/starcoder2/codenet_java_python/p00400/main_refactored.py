class main:
    import sys
    
    N = int(sys.stdin.readline())
    
    if 'A' <= N <= 'Z':
        print(1)
    elif 'a' <= N <= 'z':
        print(2)
    else:
        print(0)