class main:
    def p03482():
        S = input()
        ans = 0
        if len(S) % 2 == 0:
            if S[len(S) // 2 - 1] != S[len(S) // 2]:
                print(len(S) // 2)
                return
            else:
                S = S[:len(S) // 2] + S[len(S) // 2 + 1:]
                ans = 1
        mid = len(S) // 2
        for i in range(1, mid + 1):
            if i + mid == len(S) or S[mid + i] != S[mid] or S[mid - i] != S[mid]:
                ans += mid + i
                break
        print(ans)
    
    p03482()