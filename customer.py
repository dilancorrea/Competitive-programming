#Uva online judge 1153

from sys import stdin
import heapq
def main():
    cases = int(stdin.readline())
    for j in range(cases):
        line = stdin.readline()
        N = int(stdin.readline())
        orders = [ tuple(map(int, stdin.readline().split())) for _ in range(N) ]
        orders, queue, tons = sorted(orders, key = lambda x: x[1]), [], 0
        for i in range(N):
            tons += orders[i][0]
            heapq.heappush(queue, -orders[i][0])
            while tons > orders[i][1]: 
                N = N-1
                tons += heapq.heappop(queue)
        if j == cases-1: print(N) 
        else: print(N, end='\n\n')
main()