#Uva online judge 10344
from sys import stdin
def solve(result, numbers, operator):
    global answer
    if operator == 5:
        if result == 23: answer = 'Possible'
    else:
        i = 0
        while i < len(numbers) and answer == 'Impossible':
            if numbers[i] != -1:
                x = numbers[i]
                numbers[i] = -1
                solve(result-x, numbers, operator+1)
                solve(result*x, numbers, operator+1)
                solve(result+x, numbers, operator+1)
                numbers[i] = x
            i += 1
    return
def main():
    numbers = list(map(int, stdin.readline().split()))
    numbers.sort()
    global answer
    while numbers[0] != 0 and numbers[-1] != 0:
        answer = 'Impossible'
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                a, b = numbers[i], numbers[j]
                numbers[i], numbers[j] = -1, -1 
                solve(a-b, numbers, 2)
                solve(b-a, numbers, 2)
                solve(a+b, numbers, 2)
                solve(a*b, numbers, 2)
                numbers[i], numbers[j] = a, b
        print(answer)
        numbers = list(map(int, stdin.readline().split()))
        numbers.sort()
if __name__ == '__main__': main()