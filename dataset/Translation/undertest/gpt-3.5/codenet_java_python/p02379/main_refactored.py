class main:
    import math
    
    def main():
        lines = input().split()
        list = [float(x) for x in lines]
        
        result = math.sqrt((list[0] - list[2]) ** 2 + (list[1] - list[3]) ** 2)
        print("{:.8f}".format(result))
    
    if __name__ == "__main__":
        main()