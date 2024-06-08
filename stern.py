#Uva online judge 10077

from sys import stdin
def main():
    n, m = map( int, stdin.readline().split() )
    while m != 1 or n != 1:
        parent_left, parent_right, mid = [0,1], [1,0], [1,1]
        while mid[0] != n or mid[1] != m:
            if ( mid[0]*m ) > ( mid[1]*n ):
                print('L', end='')
                parent_right = mid
                mid = [mid[0]+parent_left[0], mid[1]+parent_left[1]]
            else:
                print('R', end='')
                parent_left = mid
                mid = [mid[0]+parent_right[0], mid[1]+parent_right[1]]
        print()
        n, m = map( int, stdin.readline().split() )
if __name__ == '__main__':
    main()