class main:
    import sys
    
    def solve(l, k):
        dp = [[0]*(l+1) for _ in range(2)]
        dp[0][0] = 1
        for i in range(1, l+1):
            dp[0][i] += dp[1][i-1]
            dp[1][i] += dp[0][i-1]
            if i >= k:
                dp[1][i] += dp[0][i-k]
        ans = 0
        for i in range(1, l+1):
            ans += dp[1][i]
        return ans
    
    if __name__ == "__main__":
        l, k = map(int, sys.stdin.readline().split())
        print(solve(l, k))