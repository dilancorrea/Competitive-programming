#Uva online judge 12834

from sys import stdin

def main():
    T = int( stdin.readline() )
    for j in range( T ):
        N, K = map( int, stdin.readline().split() )
        Xi = list( map( int, stdin.readline().split()) )
        Yi = list( map( int, stdin.readline().split()) )
        pares, profit, i = list(zip(Xi, Yi)), 0, 0
        pares = sorted(pares, key=lambda x: x[1] - x[0])
        while i < N:
            if pares[i][1] - pares[i][0] < 0 and K > 0:
                K -= 1
            else:
                profit += pares[i][1] - pares[i][0]
            i += 1
        if profit <= 0: print(f'Case {j+1}: No Profit')
        else: print(f'Case {j+1}: {profit}')
if __name__ == '__main__': main()