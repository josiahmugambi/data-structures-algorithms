#Uses python3

import sys

sys.setrecursionlimit(200000)

visited = []
ccnum = []
cc = 0

def number_of_strongly_connected_components(adj):
    result = 0
    #write your code here
    reversed_adj = reverse_graph(adj)
    dfs(reversed_adj)
    result = len(set(ccnum))
    return result

def reverse_graph(adj):
    reversed_adj = [[] for _ in range(len(adj))]
    for a, b in enumerate(adj):
        for z in b:
            reversed_adj[z].append(a)
    return reversed_adj

def dfs(adj):
    global visited, cc
    visited = [False for e in visited] #mark v unvisited
    cc = 1
   # adj_reversed = adj.reverse()
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
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    data = [4,4,1,2,4,1,2,3,3,1]
    #data = [5,7,2,1,3,2,3,1,4,3,4,1,5,2,5,3]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)        

    
    visited = [False] * n
    ccnum = [None] * n
    
    print(number_of_strongly_connected_components(adj))
