#Uva online judge 10057

from sys import stdin
def find_low( low, hi, median, numbers ):
    while low != hi:
        mid = (low+( ( hi-low )>>1 ))
        if numbers[ mid ] < numbers[ median ]: low = mid+1
        else: hi = mid
    return low
def main():
    N = stdin.readline()
    while N != '':
        numbers = []
        for _ in range( int( N ) ): numbers.append( int( stdin.readline() ) )
        numbers.sort()
        median, cnt_nums, nums_diff = ( len( numbers ) // 2 )-1, 1, 1
        if len( numbers ) % 2 == 0:
            low, hi = 0, median
            low = find_low( 0, median, median, numbers )
            j, cnt_nums = median+1, median-low+1
            if numbers[ median ] != numbers[ median+1 ]:
                nums_diff += numbers[ median+1 ] - numbers[ median ]
            while j < len( numbers ) and ( numbers[ median ] == numbers[ j ] or numbers[ j ] == numbers[ median+1 ] ): j += 1
            print( numbers[ median ], cnt_nums+(j-median)-1, nums_diff )
        else:
            low, hi = 0, median+1
            low = find_low( 0, median+1, median+1, numbers )
            j, cnt_nums = median+2, median-low+1
            while j < len( numbers ) and numbers[ j ] == numbers[ median+1 ]: j += 1
            print( numbers[ median+1 ], cnt_nums+(j-median-1), nums_diff )
        N = stdin.readline()
main()