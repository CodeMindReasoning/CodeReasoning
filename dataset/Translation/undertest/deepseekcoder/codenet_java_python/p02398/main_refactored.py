class main:
    def p02398():
        x, y, z = map(int, input().split())
        t = 0
        for i in range(x, y+1):
            if z % i == 0:
                t += 1
        print(t)
    
    p02398()