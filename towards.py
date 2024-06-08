#Uva online judge 11002

from sys import stdin, setrecursionlimit

setrecursionlimit(3000)

def phi( board, N, i, j, sum, mem ):
    ans = None
    if j < 0 or j >= len(board[i]): ans = 99999
    elif i == len(board)-1: ans = abs( min( sum+board[i][j], sum-board[i][j] ) )
    elif ( i,j,sum ) in mem: ans = mem[(i,j,sum)]
    else:
        ans = 99999
        ans = min( ans, phi( board, N, i+1, j, sum+board[i][j], mem ) )
        ans = min( ans, phi( board, N, i+1, j, sum-board[i][j], mem ) )
        if i >= N-1:
            ans = min( ans, phi( board, N, i+1, j-1, sum+board[i][j], mem) )
            ans = min( ans, phi( board, N, i+1, j-1, sum-board[i][j], mem ) )
        else:
            ans = min( ans, phi( board, N, i+1, j+1, sum+board[i][j], mem ) )
            ans = min( ans, phi( board, N, i+1, j+1, sum-board[i][j], mem ) )
    mem[( i, j, sum )] = ans
    return ans

def main():
    N = int( stdin.readline() )
    global dp
    while N != 0:
        board = []
        for _ in range( (2*N)-1 ):
            board.append( list( map( int, stdin.readline().split() ) ) )
        dp = [ [ [999999 for _ in range(3000)] for _ in range(len(board[i])) ] for i in range((2*N)-1) ]
        print( phi( board, N, 0,0, 0, {}) )
        N = int( stdin.readline() )
if __name__ == '__main__': main()