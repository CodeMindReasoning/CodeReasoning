class main:
    import sys
    
    def main():
        num = [1, 4, 8, 16, 32, 64, 128, 256, 512,  9, 27, 81, 243, 729,  16, 64, 256, 1024, 25, 125, 625,  36, 216,  49, 343,  64, 512,  81, 729,  100, 1000, 121,  144,  169,  196,  225,  256,  289,  324,  361,  400, 441, 484,  529,  576,  625,  676,  729,  784,  841, 900,  961]
        num.sort()
        X = int(sys.stdin.readline())
        max = -1
        for i in range(len(num), 0, -1):
            n = num[i - 1]
            if n <= X:
                max = max if max > n else n
                break
        print(max)
    
    if __name__ == '__main__':
        main()