#Uva online judge 1344

from sys import stdin 

def main():
    N = int( stdin.readline() )
    while N != 0:
        Tian = list( map( int, stdin.readline().split() ) )
        King = list( map( int, stdin.readline().split() ) )
        Tian.sort()
        King.sort()
        Ti = Ki = cnt = i = 0
        Tj = Kj = N-1
        while i < N:
            if Tian[Ti] > King[Ki]:
                Ki, Ti, cnt = Ki+1, Ti+1, cnt + 200
            elif Tian[Tj] > King[Kj]:
                Kj, Tj, cnt = Kj-1, Tj-1, cnt + 200
            elif Tian[Ti] < King[Ki] or (Tian[Ti] == King[Ki] and Tian[Ti] < King[Kj] and Tian[Tj] <= King[Kj]):
                Ti, Kj, cnt = Ti+1, Kj-1, cnt - 200
            else:
                Ti, Ki = Ti+1, Ki+1
            i += 1
        print(cnt)
        N = int( stdin.readline() )
if __name__ == '__main__': main()