#Uses python3

import sys

visited = []

def reach(adj, x, y):
    global visited
    explore (adj, x)
    if visited [y]:
        return 1
    else:
        return 0

def explore(adj, v):
    global visited
    visited[v] = True

    for w in adj[v]:
        if not visited[w]:
            explore(adj, w)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [4,4,1,2,3,2,4,3,1,4,1,4]
    #data = [4,2,1,2,3,2,1,4]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    visited = [False] * n

    print(reach(adj, x, y))
