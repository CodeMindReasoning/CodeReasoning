class main:
    import sys
    
    def main():
        for line in sys.stdin:
            a, b = map(int, line.strip().split())
            print(a % b)
    
    if __name__ == '__main__':
        main()