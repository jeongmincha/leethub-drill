# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        answers = []
        
        def helper(node):
            if not node:
                return False
            if not node.left and not node.right:
                answers[-1].append(node.val)
                return True
            
            if helper(node.left):
                node.left = None
            if helper(node.right):
                node.right = None
            
            return False
        
        while root.left or root.right:
            answers.append([])
            helper(root)
        
        answers.append([root.val])
        
        return answers
            