class main:
    def p03377():
        a, b, x = map(int, input().split())
        if a + b >= x and a <= x:
            print("YES")
        else:
            print("NO")
    
    p03377()