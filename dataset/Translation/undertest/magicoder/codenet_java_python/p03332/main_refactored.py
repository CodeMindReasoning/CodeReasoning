class main:
    import sys
    
    M = 998244353
    
    def modI(a, m):
        if (a %= m) <= 1:
            return 1
        return ((1 - modI(m % a, a) * m) // a + m) % m
    
    def main():
        n, a, b, k = map(int, sys.stdin.readline().split())
        nck = [0] * (n + 1)
        nck[0] = 1
        for i in range(1, n + 1):
            nck[i] = nck[i - 1] * (n - i + 1) % M * modI(i, M) % M
        ans = 0
        for i in range(n + 1):
            if a * i <= k and (k - a * i) % b == 0 and (k - a * i) // b <= n:
                ans += nck[i] * nck[(k - a * i) // b] % M
        print(ans % M)
    
    if __name__ == "__main__":
        main()