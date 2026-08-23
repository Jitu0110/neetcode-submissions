# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Time - O(n) Space - O(1)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = 0
        result = 0

        def inorder(root):
            nonlocal count
            nonlocal result

            if not root or count >= k:
                return
            
            inorder(root.left)
            count+=1
            if count == k:
               result = root.val
               return 
            inorder(root.right)
        
        inorder(root)

        return result

    # Space - O(N) Time - O(N)
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


    #     inorderTraversal = []

    #     def inorder(root):
    #         if not root:
    #             return
            
    #         inorder(root.left)
    #         inorderTraversal.append(root.val)
    #         inorder(root.right)
        
    #     inorder(root)

    #     return inorderTraversal[k-1]




    
    
        