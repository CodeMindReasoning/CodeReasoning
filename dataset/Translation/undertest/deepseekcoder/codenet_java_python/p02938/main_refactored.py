class main:
    import sys
    
    MOD = 1000000007
    
    def go():
        l, r = map(int, sys.stdin.readline().split())
        n = len(bin(r)) - 2
        dp = [[[[0]*2 for _ in range(2)] for _ in range(2)] for _ in range(n+1)]
        for x in range(2):
            for y in range(2):
                for msb in range(2):
                    dp[0][x][y][msb] = 1
        for i in range(1, n+1):
            for x in range(2):
                for y in range(2):
                    for msb in range(2):
                        if x == 1 or get_bit(l, i-1) == 0:
                            dp[i][x][y][msb] += dp[i-1][x][y | get_bit(r, i-1)][msb]
                            dp[i][x][y][msb] %= MOD
                        if y == 1 or get_bit(r, i-1) == 1:
                            dp[i][x][y][msb] += dp[i-1][x | (1-get_bit(l, i-1))][y][1]
                            dp[i][x][y][msb] %= MOD
                        if (x == 1 or get_bit(l, i-1) == 0) and (y == 1 or get_bit(r, i-1) == 1) and msb == 1:
                            dp[i][x][y][msb] += dp[i-1][x][y][1]
                            dp[i][x][y][msb] %= MOD
        print(dp[n][0][0][0])
    
    def get_bit(n, i):
        return (n >> i) & 1
    
    if __name__ == "__main__":
        go()