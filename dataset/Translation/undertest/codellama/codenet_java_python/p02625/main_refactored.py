class main:
    import sys
    
    num = 1000000007
    fact = [1] * 500001
    inv = [1] * 500001
    
    for i in range(1, 500000):
        fact[i] = (fact[i-1] * i) % num
        inv[i] = power(fact[i], num-2, num) % num
    
    n, m = map(int, sys.stdin.readline().split())
    
    ans = fact[m] * inv[m-n] % num
    
    anss = 0
    pos = 1
    for i in range(1, n+1):
        prod = 1
        prod *= fact[n]
        prod %= num
        prod *= inv[i]
        prod %= num
        prod *= inv[n-i]
        prod %= num
        prod *= fact[m-i]
        prod %= num
        prod *= inv[m-n]
        prod %= num
        prod *= pos
        anss += prod
        anss = (anss + num) % num
        pos = -pos
    
    actualans = 0
    actualans += ans * ans
    actualans %= num
    actualans -= anss * ans
    actualans %= num
    actualans = (actualans + num) % num
    
    print(actualans)
    
    def power(x, y, mod):
        ans = 1
        while y > 0:
            if y % 2 == 1:
                ans = (ans * x) % mod
            x = (x * x) % mod
            y //= 2
        return int(ans)