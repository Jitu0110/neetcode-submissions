"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    #Time - O(N+E). Visit each node once, and each edge(connection) once as well
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneDict = {}

        def dfs(node):
            if node is None:
                return None

            if node in cloneDict:
                return cloneDict[node]

            clonedNode = Node(node.val)
            cloneDict[node] = clonedNode

            for neighbor in node.neighbors:
                clonedNode.neighbors.append(dfs(neighbor))

            return clonedNode

        return dfs(node)
        