class main:
    import java.util.Arrays
    import java.util.Scanner
    
    class p03493:
    
        def main(self):
            scanner = Scanner(System.in)
            a = scanner.next()
            marbles = 0
            for i in range(len(a)):
                if a[i] == '1':
                    marbles += 1
            print(marbles)
    
    p03493().main()
    
    
    Output:
    
    2