class main:
    import sys
    
    class FastScanner:
        def __init__(self, input_stream=sys.stdin):
            self.input_stream = input_stream
            self.buffer = bytearray(1024)
            self.ptr = 0
            self.buflen = 0
    
        def has_next_byte(self):
            if self.ptr < self.buflen:
                return True
            else:
                self.ptr = 0
                try:
                    self.buflen = self.input_stream.readinto(self.buffer)
                except IOError:
                    pass
                if self.buflen <= 0:
                    return False
    
        def read_byte(self):
            if self.has_next_byte():
                return self.buffer[self.ptr]
            else:
                return -1
    
        def is_printable_char(self, c):
            return 33 <= c <= 126
    
        def has_next(self):
            while self.has_next_byte() and not self.is_printable_char(self.buffer[self.ptr]):
                self.ptr += 1
            return self.has_next_byte()
    
        def next(self):
            if not self.has_next():
                raise StopIteration
            sb = []
            b = self.read_byte()
            while self.is_printable_char(b):
                sb.append(chr(b))
                b = self.read_byte()
            return "".join(sb)
    
        def next_long(self):
            if not self.has_next():
                raise StopIteration
            n = 0
            minus = False
            b = self.read_byte()
            if b == "-":
                minus = True
                b = self.read_byte()
            if b < "0" or "9" < b:
                raise ValueError
            while True:
                if "0" <= b <= "9":
                    n *= 10
                    n += ord(b) - ord("0")
                elif b == -1 or not self.is_printable_char(b):
                    return -n if minus else n
                else:
                    raise ValueError
                b = self.read_byte()
    
        def next_int(self):
            nl = self.next_long()
            if nl < sys.maxint or nl > sys.maxint:
                raise ValueError
            return int(nl)
    
        def next_double(self):
            return float(self.next())
    
    def p(element):
        print(element)
    
    def pp(element):
        print(element, end="")
    
    def min(a, b, c):
        return min(a, b, c)
    
    def max(a, b, c):
        return max(a, b, c)
    
    def main():
        sc = FastScanner()
        str = sc.next()
        str = str.replace("BC", "X")
        a = 0
        ans = 0
        for i in range(len(str) - 1, -1, -1):
            c = str[i]
            if c == "X":
                a += 1
            elif c == "A":
                ans += a
            else:
                a = 0
        p(ans)
    
    if __name__ == "__main__":
        main()