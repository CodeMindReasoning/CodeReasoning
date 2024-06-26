class main:
    def solve(s):
        n = len(s)
        count = [0] * (2 * n + 1)
        now = 0
        for i in range(n):
            if s[i] == '(':
                now += 1
            else:
                now -= 1
            count[now + n] += 1
        now = 0
        ans = 0
        for i in range(n):
            if s[i] == '(':
                now += 1
            else:
                now -= 1
            count[now + n] -= 1
            ans += count[now + n]
        return ans
    
    s = input()
    print(solve(s))