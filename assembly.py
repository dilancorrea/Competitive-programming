#Uva online judge 13082

from sys import stdin

def main():
    test_cases = int( stdin.readline() )
    for case in range( 1, test_cases + 1 ):
        N, cnt, dict = int( stdin.readline() ), 0, {}
        heights = list( map( int, stdin.readline().split() ) )
        for i in range(N): dict[ heights[i] ] = i
        i = 2
        while i <= N and N != 1 and dict[ i ] > dict[ i-1 ]: i, cnt = i+1, cnt+1 
        print(f'Case {case}: {N-cnt-1}')
if __name__ == "__main__":
    main()