class main:
    def p03389():
        A, B, C = map(int, input().split())
        M = max(A, max(B, C))
    
        if (A+B+C)%2 == M%2:
            print((3*M-(A+B+C))//2)
        else:
            print(((3*M+3)-(A+B+C))//2)
    
    p03389()