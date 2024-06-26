class main:
    import sys
    
    P = 1_000_000_007
    
    def inv(x):
        return pow(x, P-2, P)
    
    def solve():
        n = int(input())
        dp = [1, 0, 0]
        inv_ = [inv(i) for i in range(1, n+1)]
        coef = 1
        ret = 0
        for k in range(1, n+1):
            nxt = [0, 0, 0]
            for j1 in range(3):
                for j2 in range(3):
                    if j1!= j2:
                        nxt[j2] += dp[j1]
                        nxt[j2] %= P
            dp = nxt
            coef = (coef * (n-k+1) % P * inv_[k] % P) % P
            ways = (dp[1] * coef % P) % P
            delta = (inv_[3] * inv_[n] % P * inv_[k] % P * ways % P) % P
            ret += delta
        ret %= P
        for i in range(1, n):
            ret = ret * inv_[3] % P
        print(ret)
    
    if __name__ == '__main__':
        solve()