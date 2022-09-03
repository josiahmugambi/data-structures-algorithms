#Uses python3

import sys

def dfs(adj, visited, order, x):
    #write your code here
    visited[x] = True
    if len(adj[x]) > 0:
        for w in adj[x]:
            if not visited[w]:
                dfs(adj, visited, order, w)
    order.append(x)
    #return order


def toposort(adj):
    visited = [False] * len(adj)
    order = []
    #write your code here
    for v in range(len(adj)):
        if not visited[v]:
            dfs(adj, visited, order, v)
    order = order[::-1]
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = [4,3,1,2,4,1,3,1]
    #data = [4,1,3,1]
    #data = [5,7,2,1,3,2,3,1,4,3,4,1,5,2,5,3]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

