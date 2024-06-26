class main:
    class p01636:
        INF = 1 << 28
        EPS = 1e-10
    
        def run(self):
            a = input()
            ans = 0
            for i in range(len(a)):
                head = a[:i]
                tail = a[i:]
                if head == "":
                    h = 0
                elif head == "-":
                    continue
                else:
                    h = int(head)
                    
                if tail == "":
                    t = 0
                elif tail[0] == '0':
                    continue
                else:
                    t = int(tail)
                
                if t < 0:
                    continue
                if h > t:
                    continue
                if (h + t) % 2 != 0:
                    continue
                if (t - h) % 2 != 0:
                    continue
                ans += 1
            
            print(ans)
    
    if __name__ == "__main__":
        p = p01636()
        p.run()