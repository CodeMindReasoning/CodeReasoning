class main:
    import sys
    
    def calc(n, x):
        if n == 0:
            return 1
        sum = 0
        x -= 1
        length = length(n-1)
        p = p(n-1)
        if x > 0:
            if length <= x:
                sum += p
            else:
                sum += calc(n-1, x)
            x -= length
        if x > 0:
            x -= 1
            sum += 1
        if x > 0:
            if length <= x:
                sum += p
            else:
                sum += calc(n-1, x)
        return sum
    
    def length(n):
        return 1 + 4 * ((2**n) -1)
    
    def p(n):
        return 1 + 2 * ((2**n) -1)
    
    n, x = map(int, sys.stdin.readline().split())
    print(calc(n, x))