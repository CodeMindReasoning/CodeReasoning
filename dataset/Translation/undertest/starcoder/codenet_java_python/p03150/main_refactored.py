class main:
    import sys
    
    def check(s):
        if s == 'keyence':
            return True
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[:i]+s[j:] == 'keyence':
                    return True
        return False
    
    if __name__ == '__main__':
        s = sys.stdin.readline().strip()
        if check(s):
            print('YES')
        else:
            print('NO')