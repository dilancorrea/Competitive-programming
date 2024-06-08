#Uva online judge 12482

from sys import stdin
def main():
    line = stdin.readline()
    while line != '':
        N, L, C = map( int, line.split() )
        story = stdin.readline().strip().split(" ")
        npages, ncharacteres, nlines = 1, 0, 0
        for i in range(len(story)):
            if ncharacteres + len(story[i]) <= C: ncharacteres += len(story[i]) + 1
            else: nlines, ncharacteres = nlines + 1, len(story[i]) + 1
            if nlines == L: npages, nlines = npages + 1, 0
        print(npages)
        line = stdin.readline()
main()