# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root]
        
        while stack and root is not None:
            if root.left:
                stack.append(root.left)
                root = root.left
            else:
                root = stack.pop()
                root.left = None
                result.append(root.val)
                
                if root.right:
                    stack.append(root.right)
                    root = root.right
        
        return result