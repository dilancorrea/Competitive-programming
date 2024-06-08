#Uva online judge 13054

from sys import stdin
def main():
    C = int( stdin.readline() )
    for i in range( 1,C+1 ):
        N, H, Ta, Td = map( int, stdin.readline().split() )
        hipo = list( map( int, stdin.readline().split() ) )
        hipo.sort( reverse=True )
        j, sum, k = 0, 0, N-1
        while j <= k:
            if hipo[ j ]+hipo[ k ] < H and j != k and Td <= 2*Ta: j, k, sum = j + 1, k - 1, sum + Td 
            else: j, sum = j + 1, sum + Ta
        print(f'Case {i}: {sum}')
main()