class main:
    def atcoder_ABC143_A():
        A, B = map(int, input().split())
        if A - (B * 2) > 0:
            print(A - (B * 2))
    
    # Test case
    atcoder_ABC143_A()