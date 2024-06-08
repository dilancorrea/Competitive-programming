#Uva online judge 11890

from sys import stdin

def solve( n_i, n_j, ex_i, expression, numbers, sign ):
    sum = 0
    while ex_i < len(expression) and expression[ex_i] != ')':
        if expression[ex_i] == 'x':
            if sign == '-':
                if ex_i > 0 and expression[ex_i-1] == '-':
                    sum -= numbers[n_j]
                    n_j -= 1
                else:
                    sum += numbers[n_i]
                    n_i += 1
            else:
                if ex_i > 0 and expression[ex_i-1] == '-':
                    sum -= numbers[n_i]
                    n_i += 1
                else:
                    sum += numbers[n_j]
                    n_j -= 1
        if expression[ex_i] == '(':
            if ex_i > 0 and expression[ex_i-1] == '-' and expression[ex_i-1] == sign:
                tmp, n_i, n_j, ex_i = solve( n_i, n_j, ex_i+1, expression, numbers, '+')
                sum -= tmp
            elif ex_i > 0 and expression[ex_i-1] == '-' and expression[ex_i-1] != sign:
                tmp, n_i, n_j, ex_i = solve( n_i, n_j, ex_i+1, expression, numbers, '-')
                sum -= tmp
            elif ex_i > 0 and expression[ex_i-1] == '+' and expression[ex_i-1] == sign:
                tmp, n_i, n_j, ex_i = solve( n_i, n_j, ex_i+1, expression, numbers, '+')
                sum += tmp
            else:
                tmp, n_i, n_j, ex_i = solve( n_i, n_j, ex_i+1, expression, numbers, sign)
                sum += tmp
        ex_i += 1
    return sum, n_i, n_j, ex_i 

def main():
    T = int( stdin.readline() )
    for _ in range( T ):
        expression = stdin.readline().strip()
        cnt_numbers = int( stdin.readline() )
        numbers = list( map( int, stdin.readline().split() ) )
        numbers.sort()
        print( solve( 0, cnt_numbers-1, 0, expression, numbers, '+' )[0] )
if __name__ == '__main__': main()