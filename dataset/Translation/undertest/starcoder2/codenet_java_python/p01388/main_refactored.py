class main:
    s = input()
    c = [0,0,0,0]
    for i in range(len(s)):
        if s[i] == 'K':
            c[0] += 1
        if s[i] == 'U':
            c[1] += 1
        if s[i] == 'P':
            c[2] += 1
        if s[i] == 'C':
            c[3] += 1
    print(min(c))