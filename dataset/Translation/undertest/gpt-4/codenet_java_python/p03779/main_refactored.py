class main:
    x = int(input())
    ans = 0
    
    for i in range(100000):
        if x <= i * (i + 1) // 2:
            ans = i
            break
    
    print(ans)