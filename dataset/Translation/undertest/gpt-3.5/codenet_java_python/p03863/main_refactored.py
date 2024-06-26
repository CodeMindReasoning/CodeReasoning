class main:
    import io
    import sys
    
    # Function to read input from InputStream
    def input():
        return sys.stdin.readline().strip()
    
    # Function to check if a character is a space character
    def isSpaceChar(c):
        return not (c >= 33 and c <= 126)
    
    # Main function to solve the problem
    def solve():
        s = input()
        l = len(s)
    
        if (l % 2 == 0) ^ (s[0] == s[l - 1]):
            print("Second")
        else:
            print("First")
    
    if __name__ == '__main__':
        solve()