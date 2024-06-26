class main:
    import sys
    
    def solver():
        n, x = map(int, sys.stdin.readline().split())
        sum = 0
        if x == n - x:
            sum = 3 * x
            print(sum)
            return
        else:
            if x > n - x:
                sum += x + n - x
                sum += calc(x, n - x, False)
            else:
                sum += x + n - x
                sum += calc(x, n - x, False)
            print(sum)
            return
    
    def calc(x, y, first):
        sum = 0
        if x % y == 0:
            if first:
                sum += y
            sum += (x // y * 2 - 1) * y
            return sum
        else:
            if first:
                sum += y
            sum += (x // y * 2) * y
            sum += calc(y, x % y, False)
            return sum
    
    solver()