class main:
    def main():
        a = list(map(int, input().split()))
        if a[0] == 1 and a[1] == 1:
            print("Open")
        elif a[2] == 1:
            print("Open")
        else:
            print("Close")
    
    if __name__ == "__main__":
        main()