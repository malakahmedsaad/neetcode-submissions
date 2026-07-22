"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dict = {}

        def rec(node):
            if node in dict:
                return dict[node]

            copy = Node(node.val)
            dict[node] = copy

            for i in node.neighbors: 
                copy.neighbors.append(rec(i))

            return copy

        return rec(node) if node else None