class main:
    import math
    
    class Tuple:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
        def print(self):
            print(f"{self.x} {self.y}")
    
    def koch(n, a, b):
        if n == 0:
            return
    
        cos60 = math.cos(math.pi * 60 / 180)
        sin60 = math.sin(math.pi * 60 / 180)
        s = Tuple((2 * a.x + 1 * b.x) / 3, (2 * a.y + 1 * b.y) / 3)
        t = Tuple((1 * a.x + 2 * b.x) / 3, (1 * a.y + 2 * b.y) / 3)
        u = Tuple((t.x - s.x) * cos60 - (t.y - s.y) * sin60 + s.x,
                  (t.x - s.x) * sin60 + (t.y - s.y) * cos60 + s.y)
    
        koch(n - 1, a, s)
        s.print()
        koch(n - 1, s, u)
        u.print()
        koch(n - 1, u, t)
        t.print()
        koch(n - 1, t, b)
    
    def main():
        n = int(input())
        a = Tuple(0.0, 0.0)
        b = Tuple(100.0, 0.0)
    
        a.print()
        koch(n, a, b)
        b.print()
    
    if __name__ == "__main__":
        main()