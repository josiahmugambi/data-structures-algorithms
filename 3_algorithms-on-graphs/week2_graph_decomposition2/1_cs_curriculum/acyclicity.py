#Uses python3

import sys

visited = []

def acyclic(adj):
    for v in range(len(adj)):
        is_cyclic = explore(adj, v)
        if is_cyclic:
            return 1
    return 0

def explore(adj, v):
    global visited
    visited[v] = True

    for w in adj[v]:
        if visited[w]: 
            visited[v] = False
            return True
        is_cyclic = explore(adj,w)
        if is_cyclic:
            return True

    visited[v] = False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [4,4,1,2,4,1,2,3,3,1]
    #data = [5,7,1,2,2,3,1,3,3,4,1,4,2,5,3,5]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    visited = [False] * n
    print(acyclic(adj))
