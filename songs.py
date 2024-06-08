#Uva online judge 1346

from sys import stdin

def main():
    N = stdin.readline()
    while N != '':
        songs = []
        line = stdin.readline().split()
        while len(line) != 1:
            for i in range(0, len(line),3):
                tupla = (float(line[i]), float(line[i+1]), float(line[i+2]))
                songs.append(tupla)
            line = stdin.readline().split()
        songs = sorted( songs, key=lambda x: (x[2]/x[1]), reverse=True )
        print(int(songs[int(line[0])-1][0]))
        N = stdin.readline()
if __name__ == '__main__': main()