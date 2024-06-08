#Uva online judge 10074

from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)
def phi(col, C, B, S, bridge, mem):
    ans = None
    if (col >= C and B != 0): ans = 1e18
    elif B == 0: ans = 0
    elif (col,B) in mem: ans = mem[(col,B)]
    else:
        ans = bridge[col]+phi(col+S+1, C, B-1, S, bridge, mem)
        if ((B-1)*S)+col+B < C: ans = min( ans, phi(col+1, C, B, S, bridge, mem) )
        mem[(col,B)] = ans
    return ans
def dfs(row, col, R, C, lastS, mapa):
    if not (row < 0 or col < 0 or row >= R or col >= C or mapa[row][col] != '#'):
        mapa[row][col] = 'S'
        dfs( row, col + 1, R, C, lastS, mapa)
        dfs( row + 1, col, R, C, lastS, mapa)
        dfs( row, col - 1, R, C, lastS, mapa)
        dfs( row - 1, col, R, C, lastS, mapa)
        lastS[col] = min(lastS[col], row)
def main():
    Y = stdin.readline()    
    while Y != '':
        numeros = list(map(int, Y.split()))
        R, C = numeros[0], numeros[1]
        B, S = map(int, stdin.readline().split())
        bridge, lastS = [0] * (C), [1001] * (C)
        mapa = [list(input().strip()) for _ in range(R)]
        dfs( R-1, 0, R, C, lastS, mapa )
        for col in range(C):
            i = lastS[col]
            while i > 0 and mapa[i][col] != '#': i-=1
            bridge[col] = lastS[col] - i - 1
        print( phi(0, C, B, S, bridge, {}) )
        Y = stdin.readline() 
main()