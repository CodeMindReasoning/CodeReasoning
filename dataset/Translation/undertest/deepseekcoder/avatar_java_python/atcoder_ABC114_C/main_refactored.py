class main:
    def f(a, m):
        if m >= 0:
            return f(a + 3 * (10 ** m), m - 1) + f(a + 5 * (10 ** m), m - 1) + f(a + 7 * (10 ** m), m - 1)
        else:
            if '3' in str(a) and '5' in str(a) and '7' in str(a) and a <= N:
                return 1
            else:
                return 0
    
    N = int(input())
    ans = 0
    S = str(N)
    for i in range(3, len(S) - 1):
        ans += (3 ** i) - 3 * (2 ** i) + 3
    ans += f(3 * (10 ** (len(S) - 1)), len(S) - 2)
    ans += f(5 * (10 ** (len(S) - 1)), len(S) - 2)
    ans += f(7 * (10 ** (len(S) - 1)), len(S) - 2)
    print(ans)