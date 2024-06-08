#957

from sys import stdin
def main():
    Y = stdin.readline()
    while Y != '':
        P, maxPopes, yearIni, yearFinal = int(stdin.readline()), float('-inf'), 0, 0
        popes = [int(stdin.readline()) for _ in range(P)]
        for i in range(P):
            target, low, hi = popes[i] + int(Y) - 1, i, P-1
            while low <= hi:
                mid = low+((hi-low)>>1)
                if popes[mid] <= target: low = mid + 1
                else: hi = mid - 1
            if hi-i+1 > maxPopes:
                maxPopes, yearIni, yearFinal = hi-i+1, popes[i], popes[hi]
        print(maxPopes, yearIni, yearFinal)
        line = stdin.readline()
        Y = stdin.readline()
main()