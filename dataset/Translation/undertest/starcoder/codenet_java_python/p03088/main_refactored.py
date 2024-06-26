class main:
    import sys
    
    mod = 1000000007
    
    def solve(n):
    	dp = [[[[0]*5 for _ in range(5)] for _ in range(5)] for _ in range(n+1)]
    	
    	#å·¦ããç¾å¨ã®æ¡æ°ãn-2,n-1,n,çªç®ã®æå­ãããã¤ã
    	#0 -> null,1 -> A, 2 -> G,3 -> C, 4 -> T ã®ããã«ãã
    	
    	# 
    	dp[0][0][0][0] = 1
    	
    	for i in range(1,n+1):
    		for j in range(5):
    			for k in range(5):
    				for l in range(5):
    					for m in range(1,5):
    						if j == 1 and l == 2 and m == 3:
    							continue
    						if j == 1 and k == 2 and m == 3:
    							continue
    						if k == 1 and l == 2 and m == 3:
    							continue
    						if k == 1 and l == 3 and m == 2:
    							continue
    						if k == 2 and l == 1 and m == 3:
    							continue
    						
    						dp[i][k][l][m] = (dp[i][k][l][m] + dp[i-1][j][k][l])% mod
    	
    	ans = 0
    	
    	for i in range(1,5):
    		for j in range(1,5):
    			for k in range(1,5):
    				ans = (ans + dp[n][i][j][k])%mod
    	
    	return ans
    
    if __name__ == '__main__':
    	n = int(sys.stdin.readline())
    	print(solve(n))