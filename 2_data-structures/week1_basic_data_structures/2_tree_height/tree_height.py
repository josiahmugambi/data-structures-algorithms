# python3

import sys
import threading

class TreeNode:
    """
        Single Tree Node 
    """
    # constructor function
    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.children = []
    
    # update parent node
    def update_parent(self, parent):
        self.parent = parent
        
    # add child to list of children nodes
    def add_child(self, child):
        self.children.append(child)
        
def build_tree(parents):
    n = len(parents)
    nodes = [None] * n
    for i in range(n):
        nodes[i] = TreeNode(i, parents[i])
    
    for child_index in range(n):
        parent_index = nodes[child_index].parent
        if parent_index == -1:
            root = child_index
        else:
            nodes[parent_index].add_child(child_index)
    
    return nodes, root
        

def compute_height(root, nodes):
    
    # base case, 0 nodes means height of 1
    if len(nodes[root].children) == 0:
        return 1
    
    max_height = 0

    for i in range(len(nodes[root].children)):
        max_height =  max(max_height, compute_height(nodes[root].children[i], nodes) + 1)

    return max_height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
#    print(compute_height(n, parents))
    nodes, root  = build_tree(parents)
    print(compute_height(root, nodes))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
