class main:
    import sys
    
    def evenSolver(n, m, a, b, sy, sx):
        if n*m < 2*(a+b):
            return False
        if n*m == 2*(a+b) and a%2==1:
            return False
        i = 0
        j = 0
        while a>0:
            ans[sy+i][sx+j] = '<'
            ans[sy+i][sx+1+j] = '>'
            a -= 1
            if a>0:
                ans[sy+1+i][sx+j] = '<'
                ans[sy+1+i][sx+1+j] = '>'
            a -= 1
            j += 2
            if j>=m:
                j = 0
                i += 2
        while b>0:
            ans[sy+i][sx+j] = '^'
            ans[sy+i+1][sx+j] = 'v'
            b -= 1
            if b>0:
                ans[sy+i][sx+j+1] = '^'
                ans[sy+1+i][sx+1+j] = 'v'
            b -= 1
            j += 2
            if j>=m:
                j = 0
                i += 2
        return True
    
    def printSolve(t):
        if t:
            print('YES')
            for carray in ans:
                print(''.join(carray))
                print()
        else:
            print('NO')
    
    if __name__ == '__main__':
        N, M, A, B = map(int, sys.stdin.readline().split())
        ans = [['.' for i in range(M)] for j in range(N)]
        if N%2 == 0 and M%2 == 0:
            printSolve(evenSolver(N, M, A, B, 0, 0))
        elif N%2==0 or M%2==0:
            if N%2==0:
                for i in range(0, N, 2):
                    if B>0:
                        B -= 1
                        ans[i][0] = '^'
                        ans[i+1][0] = 'v'
                printSolve(evenSolver(N, M-1, A, B, 0, 1))
            else:
                for j in range(0, M, 2):
                    if A>0:
                        A -= 1
                        ans[0][j] = '<'
                        ans[0][j+1] = '>'
                printSolve(evenSolver(N-1, M, A, B, 1, 0))
        else:
            ans_ = [['<','>','^'],
                    ['^','.','v'],
                    ['v','<','>']]
            for i in range(0, N-1, 2):
                if B>0:
                    B -= 1
                    ans[i][M-1] = '^'
                    ans[i+1][M-1] = 'v'
            for j in range(0, M-1, 2):
                if A>0:
                    A -= 1
                    ans[N-1][j] = '<'
                    ans[N-1][j+1] = '>'
            if A>0 and B>0 and A%2==1:
                for i in range(0, 3):
                    for j in range(0, 3):
                        ans[N-3+i][M-3+j] = ans_[i][j]
                A -= 1
                B -= 1
                printSolve(2*(A+B)<=(N-1)*(M-1)-4 and evenSolver(N-1,M-1,A,B,0,0))
            else:
                printSolve(evenSolver(N-1,M-1,A,B,0,0))