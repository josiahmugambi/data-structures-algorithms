#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

key_max = 2147483648
key_min = -2147483648
 
class Node: 
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def read():
    n = int(sys.stdin.readline())
    
    if n == 0 or n == 1:
        return n, 0
    
    key = [0 for i in range(n)]
    left = [0 for i in range(n)]
    right = [0 for i in range(n)]
    for i in range(n):
        [a, b, c] = map(int, sys.stdin.readline().split())
        key[i] = a
        left[i] = b
        right[i] = c
        


    tree = [Node(key[i], left[i], right[i]) for i in range(n)]
    
    for i in range(n):
        if tree[i].left != -1:
            temp = tree[i].left
            tree[i].left = tree[temp]
        if tree[i].right != -1:
            temp = tree[i].right
            tree[i].right = tree[temp]
    return n, tree[0]

def IsBinarySearchTree(tree):
    return (IsBST_helper(tree, key_min, key_max))
 
def IsBST_helper(node, k_min, k_max):
     
    if node == -1 or node == None:
        return True
 
    if node.key < k_min or node.key > k_max:
        return False

    return (
        IsBST_helper(node.left, k_min, node.key - 1) 
            and
        IsBST_helper(node.right, node.key + 1, k_max ))

def main():
    n, root = read()
    if n == 0 or n == 1:
        print("CORRECT")
    else:
        if IsBinarySearchTree(root):
            print("CORRECT")
        else:
            print("INCORRECT")

threading.Thread(target=main).start()