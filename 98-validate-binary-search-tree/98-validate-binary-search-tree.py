# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = True
    
    def traverseInorder(self, root: Optional[TreeNode]):
        if root is None:
            return
        
        if root.left:
            self.traverseInorder(root.left)
        if root.val > self.lastFound:
            self.lastFound = root.val
        else:
            self.answer = False
        if root.right:
            self.traverseInorder(root.right)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.lastFound = -2 ** 31 - 1
        self.answer = True
        self.traverseInorder(root);
        
        return self.answer
        
        