class main:
    import math
    
    def solve():
        N = int(input())
        for h in range(1, 3501):
            for n in range(1, 3501):
                if (4 * h * n - N * n - N * h != 0) and (N * h * n) % (4 * h * n - N * n - N * h) == 0:
                    print(h, n, (N * h * n) // (4 * h * n - N * n - N * h))
                    return
    
    solve()