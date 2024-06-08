#UVa online judge 11157

from sys import stdin
def main():
    cases = int( stdin.readline() )
    for i in range( cases ):
        N, D = map( int, stdin.readline().split() )
        rocks, j, maxi, last = [ item.split('-') for item in stdin.readline().split() ], 0, 0, 0
        while j < N:
            if rocks[j][0] == 'B':
                maxi, last = max(maxi, int(rocks[j][1])-last), int(rocks[j][1])
            elif rocks[j][0] == 'S': 
                maxi, last, rocks[j][0] = max(maxi, int(rocks[j][1])-last), int(rocks[j][1]), 'F'
            if j+1 < N and rocks[j+1][0] == 'B': j += 1
            else: j+=2
        maxi, last = max(maxi, D-last), D
        for j in range(N-1,-1,-1):
            if rocks[j][0] != 'F': maxi, last = max(maxi, last-int(rocks[j][1])), int(rocks[j][1])
        print("Case {}: {}".format(i+1,max(maxi, last)))
main()