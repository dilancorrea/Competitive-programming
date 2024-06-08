#Uva online judge 11407

import sys
sys.setrecursionlimit(10010)
def solve( number ):
    if number == 0: return 0
    if memory[ number ] != float('inf'): return memory[ number ]
    i = 1
    while i*i <= number: memory[ number ], i = min( memory[ number ], 1 + solve(number-i*i) ), i + 1
    return memory[ number ]
def main():
    global memory
    cases, memory = int(sys.stdin.readline()), [ 1 if i == 1 else float('inf') for i in range(10001) ]
    for _ in range(cases):
        number = int(sys.stdin.readline())
        print( solve( number ) )
main()