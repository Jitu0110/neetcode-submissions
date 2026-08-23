# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        result = []

        q = deque()
        q.append(root)

        while q:
            queueLength = len(q)
            for i in range(queueLength):
                item = q.popleft()

                if(i==queueLength-1):
                  result.append(item.val)

                if item.left:
                    q.append(item.left)
                
                if item.right:
                    q.append(item.right)
        
        return result
        