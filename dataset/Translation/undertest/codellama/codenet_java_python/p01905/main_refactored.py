class main:
    import sys
    
    class p01905:
        def __init__(self):
            self.N = int(sys.stdin.readline())
            self.M = int(sys.stdin.readline())
            self.a = [int(x) for x in sys.stdin.readline().split()]
            self.b = [True] * (self.N * 2 - 1)
            for i in range(self.M):
                self.b[self.a[i] + self.N - 1] = False
            for i in range(self.N * 2 - 2, 0, -2):
                if self.b[i] and self.b[i - 1]:
                    self.b[(i - 2) // 2] = True
                elif self.b[i] or self.b[i - 1]:
                    self.b[(i - 2) // 2] = True
                else:
                    self.b[(i - 2) // 2] = False
            self.ans = 0
            for i in range(self.N - 1):
                if self.b[i * 2 + 1] and self.b[i * 2 + 2]:
                    self.ans += 1
            print(self.ans)
    
    if __name__ == "__main__":
        p01905().solve()