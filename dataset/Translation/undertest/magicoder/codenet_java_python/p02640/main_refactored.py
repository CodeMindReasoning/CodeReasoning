class main:
    import sys
    
    def main():
        x, y = map(int, sys.stdin.readline().split())
        crane = -(y/2) + 2*x
        turtle = x - crane
        if turtle < 0 or crane < 0 or turtle % 1 != 0 or crane % 1 != 0:
            print("No")
        else:
            print("Yes")
    
    if __name__ == "__main__":
        main()