#Uva online judge 11813

from sys import stdin
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def minDistance(self, dist, sptSet):

        min = 100001

        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
 
        return min_index

    def dijkstra(self, src):
        dist = [100001] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
            x = self.minDistance(dist, sptSet)

            sptSet[x] = True
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
 
        return dist
 
def main():
    cases = int( stdin.readline() )
    for _ in range( cases ):
        N, M = map( int, stdin.readline().split() )
        g = Graph( N )
        for _ in range( M ):
            X, Y, D = map( int, stdin.readline().split() )
            g.graph[X][Y] = D
            g.graph[Y][X] = D
        S = int( stdin.readline() )
        dict = {}
        dict[0] = g.dijkstra(0)
        for _ in range( S ):
            Si = int( stdin.readline() )
            dict[Si] = g.dijkstra( Si )
        
if __name__ == '__main__': main()
