class main:
    import sys
    
    def main():
        A, B, C = map(int, sys.stdin.readline().split())
    
        array = [A, B, C]
        array.sort()
    
        if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
            print(0)
        else:
            print(array[0] * array[1])
    
    if __name__ == "__main__":
        main()