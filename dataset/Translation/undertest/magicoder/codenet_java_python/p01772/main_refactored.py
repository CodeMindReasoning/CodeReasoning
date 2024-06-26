class main:
    class MyScanner:
        def read(self):
            try:
                return input()
            except EOFError:
                raise EOFError
    
        def isSpaceChar(self, c):
            return c == ' ' or c == '\n' or c == '\r' or c == '\t' or c == -1
    
        def isEndline(self, c):
            return c == '\n' or c == '\r' or c == -1
    
        def next(self):
            c = self.read()
            while self.isSpaceChar(c):
                c = self.read()
            res = ''
            while not self.isSpaceChar(c):
                res += c
                c = self.read()
            return res
    
        def nextLine(self):
            c = self.read()
            while self.isEndline(c):
                c = self.read()
            res = ''
            while not self.isEndline(c):
                res += c
                c = self.read()
            return res
    
    
    def run():
        sc = MyScanner()
    
        c = sc.next()
        n = len(c)
        s = ''
        for i in range(n):
            if c[i] == 'A' or c[i] == 'Z':
                s += c[i]
        c = s
        n = len(c)
        s = ''
        for i in range(n):
            if len(s) == 0 or s[-1] != c[i]:
                s += c[i]
        if 0 < len(s) and s[0] == 'Z':
            s = s[1:]
        if 0 < len(s) and s[-1] == 'A':
            s = s[:-1]
        if 0 < len(s):
            print(s)
        else:
            print(-1)
    
    
    if __name__ == "__main__":
        run()