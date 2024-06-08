#Uva Online Judge 208
from sys import stdin
def solve(node, N, graph, visited, partial_result):
    global result
    visited[node] = True
    if node == N:
        result += 1
        for i in range(len(partial_result)):
            if i == len(partial_result)-1:
                print(partial_result[i])
            else:
                print(partial_result[i], end = ' ')
    else:
        for i in graph[node]:
            if visited[i] == False:
                partial_result.append(i)
                solve(i, N, graph, visited, partial_result)
                partial_result.pop()
                visited[i] = False
    return
def main():
    N = stdin.readline()
    cnt = 1
    global result
    while N != '':
        result, N = 0, int(N)
        graph, visited = [], []
        for _ in range(N+1):
            graph.append([])
            visited.append(False)
        nodes = list(map(int, stdin.readline().split()))
        while nodes[0] != 0 and nodes[1] != 0:
            x, y = nodes[0], nodes[1]
            if x >= len(visited)-1 or y >= len(visited)-1:
                for _ in range(max(x,y)-(len(visited)-1)):
                    graph.append([])
                    visited.append(False)
            graph[x].append(y)
            graph[y].append(x)
            nodes = list(map(int, stdin.readline().split()))
        graph = [sorted(sublist) for sublist in graph] 
        print(f'CASE {cnt}:')
        solve(1, N, graph, visited,[1])
        print(f'There are {result} routes from the firestation to streetcorner {N}.')
        cnt += 1
        N = stdin.readline()
if __name__ == '__main__': main()