#Uva online judge 13142

from sys import stdin
def search( low, hi, distance, T, S ):
    while low <= hi:
        mid = (low+hi)//2
        if distance - ( ( S+mid )*T ) <= 0:
            hi = mid-1
        else:
            low = mid+1
    return low
def main():
    cases = int( stdin.readline() )
    for _ in range( cases ):
        T, S, D = map( int, stdin.readline().split() )
        T, D = T*86400, D*1000000
        distance = (T * S) + D
        low = search( -999999, 999999, distance, T, S )
        if low <= 0: print(f'Add {abs(low)} tons')
        elif low-1 == 0: print(f'Add {abs(low-1)} tons')
        else: print(f'Remove {low-1} tons')
main()