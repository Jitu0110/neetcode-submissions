# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        return abs(self.heightOfTree(root.left) - self.heightOfTree(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
         

    

    def heightOfTree(self,root):

        def dfs(root):
            if root is None:
                return 0
            
            return 1 + max(dfs(root.left),dfs(root.right))

        return dfs(root)

        