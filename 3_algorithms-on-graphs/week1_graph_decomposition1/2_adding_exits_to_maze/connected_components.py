#Uses python3

import sys

visited = []
ccnum = []
cc = 0

def number_of_components(adj):

    dfs(adj)
    result = len(set(ccnum))
    return result
    
def dfs(adj):
    global visited, cc
    visited = [False for e in visited] #mark v unvisited
    cc = 1
    for w in range(len(adj)):
        if not visited[w]:
            explore(adj, w)
            cc += 1

def explore(adj, v):
    global visited, ccnum, cc
    visited[v] = True
    ccnum [v] = cc
    for w in adj[v]:
        if not visited[w]:
            explore(adj, w)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
   # data = [4,2,1,2,3,2]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    visited = [False] * n
    ccnum = [None] * n

    print(number_of_components(adj))
