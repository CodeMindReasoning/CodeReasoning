class main:
    import sys
    
    n = int(input())
    
    if n == 1:
        print(0)
        sys.exit()
    
    pMap = {}
    for i in range(2, int(n ** 0.5) + 1):
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 0:
            pMap[i] = count
    
    ans = 0
    for pCount in pMap.values():
        i = 1
        while pCount >= i:
            pCount -= i
            ans += 1
            i += 1
    
    print(ans)