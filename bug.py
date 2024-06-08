#Uva online judge 1216
from sys import stdin
import math
def prim(graph, rt):
  visited = [ False for _ in range(len(graph))]
  key = [ float('inf') for _ in range(len(graph))]
  key[0] = 0
  for _ in range(len(graph)):
    u = min(range(len(graph)), key=lambda i: key[i] if not visited[i] else float('inf'))
    visited[u] = True
    for v in range(len(graph)):
      if not visited[v] and graph[u][v] < key[v]:
        key[v] = graph[u][v]
  key = sorted(key)
  print(math.ceil(key[len(key)-rt]))
def main():
  W = int(stdin.readline())
  for _ in range(W):
    rt = int(stdin.readline())
    node = list( map(int, stdin.readline().split()) )
    sensors = []
    while node[0] != -1:
      sensors.append((node[0], node[1]))
      node = list( map(int, stdin.readline().split()) )
    graph = [[0] * len(sensors) for _ in range(len(sensors))]
    max = 0
    for i in range(len(sensors)):
        for j in range(i+1, len(sensors)):
            d = math.sqrt((sensors[i][0]-sensors[j][0])**2 + (sensors[i][1]-sensors[j][1])**2)
            graph[i][j] = d
            graph[j][i] = d
            if graph[i][j] > max: max = graph[i][j]
    if rt == 0 or rt >= len(sensors): print(math.ceil(max))
    else: prim(graph,rt) 
main()