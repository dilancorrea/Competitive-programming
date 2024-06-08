#Uva online judge 1395

from sys import stdin
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

def kruskal(N,edges):
    min_diff = 999999
    edges.sort(key=lambda edge: (edge[2], edge[1]))
    for i in range(len(edges)):
        uf, edges_used, j = UnionFind(N), 0, i
        while j < len(edges) and edges_used != N-1:
            if uf.union(edges[j][0], edges[j][1]):
                edges_used += 1
            j += 1
        if edges_used == N-1:
            if edges[j-1][2] - edges[i][2] >= 0:
                min_diff = min( min_diff, edges[j-1][2] - edges[i][2] )
    return min_diff
    
def main():
    N, M = map( int, stdin.readline().split() )
    while N != 0 or M != 0:
        nodes_used, edges = 0, []
        visited = [False for _ in range(N+1)]
        for _ in range(M):
            l = list( map( int, stdin.readline().split() ) )
            edges.append( (l[0], l[1], l[2]) )
            if visited[l[0]] == False:
                visited[l[0]] = True
                nodes_used += 1
            if visited[l[1]] == False:
                visited[l[1]] = True
                nodes_used += 1
        if nodes_used < N or M == 0: print(-1)
        else:
            result = kruskal(N, edges)
            if result == 999999: print(-1)
            else: print(result)
        N, M = map( int, stdin.readline().split() )
if __name__ == '__main__': main()