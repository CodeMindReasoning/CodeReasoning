class main:
    import sys
    
    def main():
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        d = [sys.maxsize] * (n + 1)
        d[0] = 0
        for i in range(n + 1):
            for j in range(3):
                if i - a[j] >= 0 and d[i - a[j]] != -1:
                    d[i] = max(d[i], d[i - a[j]] + 1)
        print(d[n])
    
    if __name__ == "__main__":
        main()