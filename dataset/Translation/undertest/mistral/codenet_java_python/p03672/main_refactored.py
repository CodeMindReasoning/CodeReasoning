class main:
    s = input()
    s1 = ""
    s2 = ""
    answer = ""
    
    for i in range(len(s)-2, -1, -2):
        s1 = s[:i]
        s2 = s[i:]
        if s1 == s2 and len(s) != len(s1):
            answer = s
            break
    
    print(len(answer))