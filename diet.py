#Uva online judge 12621

from sys import stdin
def knapSack( W, wt, n, mem ):
    if n < 0 and W > 0: return 99999
    if n < 0 or W < 0: return 0
    if( n, W ) in mem: return mem[(n,W)]
    else:
        result = min( wt[n]+knapSack( W-wt[n], wt, n-1, mem ), knapSack( W, wt, n-1, mem ) )
    mem[(n,W//10)] = result
    return result
def main():
    cases = int( stdin.readline() )
    for i in range( cases ):
        global mini
        N = int( stdin.readline() )
        cnt_courses = int( stdin.readline() )
        courses = list( map( int, stdin.readline().split() ) )
        mem = {}
        ans = knapSack( N, courses, cnt_courses-1, mem )
        if ans == 99999: print("NO SOLUTION")
        else: print(ans)
if __name__ == '__main__': main()