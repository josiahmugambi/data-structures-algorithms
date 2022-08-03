#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

key_max = 2147483648
key_min = -2147483648
 
class TreeNode: 
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def IsBinarySearchTree(tree):
    return (IsBST_helper(tree, key_min, key_max))
 
def IsBST_helper(node, k_min, k_max):
     
    if node == None:
        return True
 
    if node.key < k_min or node.key > k_max:
        return False

    return (
            IsBST_helper(node.left, k_min, node.key - 1) 
            and
            IsBST_helper(node.right, node.key + 1, k_max ))

def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
