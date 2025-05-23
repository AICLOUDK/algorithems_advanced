# python3
import sys
import threading

sys.setrecursionlimit(10**6)
threading.stack_size(2**26)

class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []

def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for _ in range(size - 1):
        a, b = map(int, input().split())
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree

def dfs(tree, vertex, parent):
    incl = tree[vertex].weight
    excl = 0
    for child in tree[vertex].children:
        if child != parent:
            c_incl, c_excl = dfs(tree, child, vertex)
            incl += c_excl
            excl += max(c_incl, c_excl)
    return incl, excl

def MaxWeightIndependentTreeSubset(tree):
    if not tree:
        return 0
    incl, excl = dfs(tree, 0, -1)
    return max(incl, excl)

def main():
    tree = ReadTree()
    print(MaxWeightIndependentTreeSubset(tree))

threading.Thread(target=main).start()