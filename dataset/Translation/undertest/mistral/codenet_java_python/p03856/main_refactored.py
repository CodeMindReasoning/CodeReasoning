class main:
    import sys
    
    def read_line():
        line = input()
        if line == "":
            exit(0)
        return line
    
    def read_token():
        while True:
            line = read_line()
            if line == "":
                exit(0)
            tokens = line.strip().split()
            if len(tokens) == 0:
                continue
            return tokens[0]
    
    def main():
        qq = int(sys.stdin.readline())
        for casenum in range(1, qq+1):
            s = read_token()
            good = ["dream", "dreamer", "erase", "eraser"]
            poss = [False] * (len(s)+1)
            poss[0] = True
            for i in range(len(s)):
                if not poss[i]:
                    continue
                for out in good:
                    if i + len(out) > len(s):
                        continue
                    match = 0
                    for a in range(len(out)):
                        if s[i+a] == out[a]:
                            match += 1
                    if match == len(out):
                        poss[i+match] = True
            print("YES" if poss[len(s)] else "NO")
    
    if __name__ == "__main__":
        main()