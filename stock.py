#Uva online judge 12951

from sys import stdin
import sys
sys.setrecursionlimit(2**29)

def solve( p, C, i, mem, status ):
    if i == len(p): return 0
    if (i,status) in mem: return mem[ (i, status) ]
    else:
        if status == 0: result = max( solve( p, C, i+1, mem, status ), solve( p, C, i+1, mem, 1 )-p[i] )
        else: result = max( solve( p, C, i+1, mem, status ), solve( p, C, i+1, mem, 0 )+( p[i]-C ) )
    mem[ (i, status) ] = result
    return result

def main():
    line = stdin.readline()
    while line!='':
        mem = {}
        N,C = map(int, line.split())
        p = list(map(int, stdin.readline().split()))
        print(solve( p, C, 0, {}, 0))
        line = stdin.readline()
main()