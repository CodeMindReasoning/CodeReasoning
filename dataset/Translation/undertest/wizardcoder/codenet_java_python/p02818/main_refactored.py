class main:
    import sys
    
    A, B, K = map(int, sys.stdin.readline().split())
    
    if K <= A:
        A -= K
    elif K <= A+B:
        B -= K-A
        A = 0
    else:
        A = 0
        B = 0
    
    print(A, B)