class main:
    import sys
    
    def solve(n):
        for i in range(1, 3510):
            for j in range(1, 3510):
                si = n * i * j
                bo = 4 * i * j - n * j - n * i
                if bo <= 0:
                    continue
                if si % bo == 0:
                    return i, j, si // bo
    
    n = int(sys.stdin.readline())
    i, j, k = solve(n)
    print(i, j, k)