class main:
    import sys
    
    class Stack:
        def __init__(self):
            self.stack = []
    
        def push(self, value):
            self.stack.append(value)
    
        def pop(self):
            return self.stack.pop()
    
        def isEmpty(self):
            return len(self.stack) == 0
    
        def isFull(self):
            return len(self.stack) == 200
    
    def main():
        stack = Stack()
        for line in sys.stdin:
            for s in line.split():
                if s == '+':
                    stack.push(stack.pop() + stack.pop())
                elif s == '-':
                    first = stack.pop()
                    second = stack.pop()
                    stack.push(second - first)
                elif s == '*':
                    stack.push(stack.pop() * stack.pop())
                else:
                    stack.push(int(s))
        print(stack.pop())
    
    if __name__ == '__main__':
        main()