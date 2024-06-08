#Uva Online Judge 13190

from sys import stdin
import heapq
def main():
    T = int( stdin.readline() )
    for _ in range( T ):
        n, k = map( int, stdin.readline().split() )
        medicine, dict = [], {}
        for i in range( n ): 
            x, y =  stdin.readline().split()
            y = int(y)
            dict[x] = y
            medicine.append( ( y,i,x ) )
        medicine = sorted( medicine, key=lambda x: ( x[0], x[1] ) )
        for _ in range( k ):
            tmp = heapq.heappop(medicine)
            print( tmp[0], tmp[2] )
            tmp = ( tmp[0]+dict[tmp[2]], tmp[1], tmp[2] )
            heapq.heappush( medicine, tmp )
main()