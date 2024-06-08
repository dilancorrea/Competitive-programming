#Uva online judge 1350

from sys import stdin
MAX = 90000000
def phi( k ):
    ans = None
    if k == 0: ans = 0
    else:
        n = 0
        while g[n+1] <= k: n += 1
        ans = (1<<n) + phi( k - g[ n ] )
    return ans
def main():
    T = int( stdin.readline() )
    global f, g
    f, g = [1,1],[1,2]
    while g[-1]< MAX:
        g.append( g[ -1 ]+f[ -1 ] )
        f.append( f[ -2 ]+f[ -1 ] )
    for _ in range(T): print( format( phi( int( stdin.readline() ) ), 'b' ) )
main()