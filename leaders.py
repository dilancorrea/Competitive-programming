#Uva Online Judge 10475
from sys import stdin
def solve(restricted, i, cnt, t, topic, sorted_words, answer, s):
    if cnt == s:
        print(' '.join(answer))
    else:
        j = i+1
        while j < t:
            flag = True
            k = 0
            while k < len(topic) and flag == True:
                if j in restricted[topic[k]]: flag = False
                k+=1
            if flag == True:
                topic.append(j)
                answer.append(sorted_words[j])
                solve(restricted, j, cnt+1, t, topic, sorted_words, answer, s)
                answer.pop()
                topic.pop()
            j += 1
    return
def main():
    cases = int(stdin.readline())
    for z in range(cases):
        t, p, s = map(int, stdin.readline().split())
        words = [ stdin.readline().strip().upper() for _ in range(t) ]
        sorted_words = sorted(words, key=lambda x: (-len(x), x))
        dict_words, restricted = {}, []
        for i in range(t):
            dict_words[sorted_words[i]] = i
            restricted.append([])
        for _ in range(p):
            tuples = stdin.readline().strip().split()
            restricted[dict_words[tuples[0].upper()]].append(dict_words[tuples[1].upper()])
            restricted[dict_words[tuples[1].upper()]].append(dict_words[tuples[0].upper()])
        print(f'Set {z+1}:')
        for i in range(t-s+1):
            solve(restricted, i, 1, t, [i], sorted_words, [f'{sorted_words[i]}'], s)
        print()
if __name__ == '__main__': main()