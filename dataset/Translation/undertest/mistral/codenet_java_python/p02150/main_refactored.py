class main:
    import sys
    
    MOD = 1000000007
    
    def main():
        a, b, x = map(int, sys.stdin.readline().split())
        s = a - b
        count = max(x - a, 0) // integer division
        total = (count % MOD) * (a % MOD) % MOD
        x -= count * s
        while x >= a:
            total += a
            x += a - b
        total %= MOD
        print(total)
    
    if __name__ == "__main__":
        main()