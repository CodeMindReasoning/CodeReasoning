class main:
    import sys
    
    def p02116():
        try:
            str = sys.stdin.readline().strip()
            res = 0
            han = 0
            ni_beki = 1
            ruijyo = 0
    
            if str == "":
                sys.exit(0)
            else:
                res = int(str)
    
                while True:
                    han = (res >> ruijyo) % 2
                    if han == 0:
                        res = (res % ni_beki) + 1
                        break
                    else:
                        ni_beki = ni_beki * 2
                        ruijyo += 1
    
            print(res)
        except Exception as e:
            e.printStackTrace()
    
    if __name__ == "__main__":
        p02116()