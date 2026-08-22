"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        linkedDist = {}

        def createDeepCopy(node):
            if node is None:
                return None

            if node in linkedDist:
                return linkedDist[node]

            newNode = Node(node.val)

            linkedDist[node] = newNode

            newNode.next = createDeepCopy(node.next)
            newNode.random = createDeepCopy(node.random)

            return newNode

        return createDeepCopy(head)