class main:
    def count(s):
        p = 1
        cnt = 1
        res = 0
        
        while p * 10 < s:
            less3 = (p * 10 - 1) // 3 - (p - 1) // 3
            less5 = (p * 10 - 1) // 5 - (p - 1) // 5
            less15 = (p * 10 - 1) // 15 - (p - 1) // 15
            
            res += ((p * 10 - 1) - (p - 1) - less3 - less5 + less15) * cnt
            res += (less3 - less15) * 4
            res += (less5 - less15) * 4
            res += less15 * 8
            
            cnt += 1
            p *= 10
            
        less3 = (s - 1) // 3 - (p - 1) // 3
        less5 = (s - 1) // 5 - (p - 1) // 5
        less15 = (s - 1) // 15 - (p - 1) // 15
        
        res += ((s - 1) - (p - 1) - less3 - less5 + less15) * cnt
        res += (less3 - less15) * 4
        res += (less5 - less15) * 4
        res += less15 * 8
        
        return res
    
    if __name__ == '__main__':
        s = int(input())
        
        upper = s
        lower = 1
        
        while upper - lower > 1:
            med = (upper + lower) // 2
            dist = count(med)
            
            if dist > s:
                upper = med
            elif dist < s:
                lower = med
            else:
                upper = med
                lower = med - 1
        
        i = lower
        cur = count(lower) + 1
        
        while True:
            if i % 15 == 0:
                str_i = "FizzBuzz"
            elif i % 3 == 0:
                str_i = "Fizz"
            elif i % 5 == 0:
                str_i = "Buzz"
            else:
                str_i = str(i)
            
            for ch in str_i:
                if cur < s:
                    pass
                elif cur >= s + 20:
                    print()
                    exit()
                else:
                    print(ch, end='')
                cur += 1
            i += 1