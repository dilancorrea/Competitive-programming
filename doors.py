#Uva online judge 10606

from sys import stdin
def main():
    N = int( stdin.readline() )
    while N != 0:
        low, hi = 1, N
        while low <= hi:
            mid = (low+hi)//2
            if mid*mid <= N: low = mid+1
            else: hi = mid-1
        print(hi*hi)
        N = int( stdin.readline() )
main()