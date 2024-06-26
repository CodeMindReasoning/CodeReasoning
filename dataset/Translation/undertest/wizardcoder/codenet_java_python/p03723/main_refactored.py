class main:
    import sys
    
    def main():
        A, B, C = map(int, input().split())
    
        count = 0
        while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
            if A == B and B == C:
                print(-1)
                return
            a = A
            b = B
            c = C
            A = (b + c) // 2
            B = (a + c) // 2
            C = (a + b) // 2
            count += 1
    
        print(count)
    
    if __name__ == '__main__':
        main()