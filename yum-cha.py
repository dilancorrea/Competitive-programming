#Uva online judge 11566

from sys import stdin
import math
N, x, T, K = None, None, None, None

def solve(acumulate, mem, dims, sum_favour, i, cant_dishes):
    ans, ans1, ans2 = 0, 0, 0
    if i == K: ans = 0
    elif (i, cant_dishes, acumulate) in mem: return mem[ (i, cant_dishes, acumulate) ]
    else:
        sum = (dims[i][0])*1.1
        if (acumulate+sum)/(N+1) <= x and cant_dishes+1 <= 2*(N+1):
            ans1 = solve(acumulate+sum, mem, dims, sum_favour, i+1, cant_dishes+1)+sum_favour[i]
        if (acumulate+(2*sum))/(N+1) <= x and cant_dishes+2 <= 2*(N+1):
            ans2 = solve(acumulate+(2*sum), mem, dims, sum_favour, i+1, cant_dishes+2)+2*sum_favour[i]
        ans = solve(acumulate, mem, dims, sum_favour, i+1, cant_dishes)
    mem[ (i, cant_dishes, acumulate) ] = max(ans, ans1, ans2)
    return max(ans, ans1, ans2)

def main():
    global N, x, T, K
    cont = 1
    line = stdin.readline().strip()
    while line == '' or line[0] != "0":
        if line == "":
            line = stdin.readline().strip()
            continue
        N, x, T, K = map(int,line.split())
        dims = [ list(map(int, stdin.readline().split())) for _ in range(K) ]
        sum_favour = [ sum(dims[i][1:]) for i in range(K) ]
        print("{:.2f}".format(solve(T*(N+1)*(1.1),{},dims,sum_favour,0, 0)/(N+1)))
        line = stdin.readline().strip()
main()