class main:
    import sys
    
    def main():
        a, b, c, d = map(int, sys.stdin.readline().split())
        sum = 0
        if d <= a:
            print(d)
            return
        sum = a
        d -= a
        if d <= b:
            print(sum)
            return
        d -= b
        sum -= d
        print(sum)
    
    if __name__ == "__main__":
        main()