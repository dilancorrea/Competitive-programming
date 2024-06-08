#Uva online judge 12259

from sys import stdin

def main():
    cases = int( stdin.readline() )
    for _ in range(cases):
        p, n = map(int, stdin.readline().split())
        contributions = list(map(int, stdin.readline().split()))
        contributions = list(enumerate(contributions))
        contributions = sorted(contributions, key=lambda x: (x[1], -x[0]))
        answer, i = {}, 0
        while i < len(contributions):
            partial_amount = p // n
            if partial_amount >= contributions[i][1]:
                p -= contributions[i][1]
                answer[contributions[i][0]] = contributions[i][1]
            else:
                p -= partial_amount 
                answer[contributions[i][0]] = partial_amount
            n -= 1
            i += 1
        if p > 0: print('IMPOSSIBLE')
        else:
            for i in range(len(contributions)): 
                if i == len(contributions)-1:
                    print(answer[i])
                else:
                    print(answer[i], end=' ')
if __name__ == "__main__":
    main()