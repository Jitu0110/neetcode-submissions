# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Time - O(n) Space - O(h) (recursive stack)
    def goodNodes(self, root: TreeNode) -> int:

        goodNodes = 0

        def dfs(root, max):
            if not root:
                return

            nonlocal goodNodes

            if root.val >= max:
                max = root.val
                goodNodes += 1
            dfs(root.left,max)
            dfs(root.right,max)

        dfs(root, float("-inf"))

        return goodNodes
        