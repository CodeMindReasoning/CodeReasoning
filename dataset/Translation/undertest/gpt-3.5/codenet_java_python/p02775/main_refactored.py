class main:
    class P02775:
        def run(self):
            N = "0" + input()
            l = len(N)
    
            # 0 おつり, 1 つめたり, 2 多く
            dp = [[0] * 3 for _ in range(l + 1)]
    
            dp[0][0] = dp[0][2] = 1
    
            for i in range(1, l):
                c = int(N[i])
                dp[i][0] = min(dp[i - 1][0], dp[i - 1][2]) + 9 - c
                dp[i][1] = min(dp[i - 1][0] + 1, dp[i - 1][1]) + c
                dp[i][2] = min(dp[i - 1][0] + 1, dp[i - 1][1]) + c + 1
    
            dp[l - 1][0] += 1
            print(min(dp[l - 1][0], min(dp[l - 1][1], dp[l - 1][2])))
    
    
    if __name__ == "__main__":
        p02775 = P02775()
        p02775.run()