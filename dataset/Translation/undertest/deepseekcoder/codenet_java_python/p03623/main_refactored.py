class main:
    def p03623():
        x, a, b = map(int, input().split())
        if abs(x-a) < abs(x-b):
            print("A")
        else:
            print("B")
    
    p03623()