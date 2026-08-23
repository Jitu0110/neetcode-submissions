# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        result = None

        while True:
            if (p.val <= root.val and q.val >= root.val) or (q.val <= root.val and p.val >= root.val):
                result = root
                break
            
            elif (p.val <root.val and q.val < root.val):
                root = root.left

            elif (q.val > root.val and p.val > root.val ):
                root = root.right
        
        return result

        



        