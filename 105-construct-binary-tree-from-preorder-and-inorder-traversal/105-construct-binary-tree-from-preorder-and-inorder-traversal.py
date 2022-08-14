# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        if len(preorder) == 0:
            return None
        
        rootVal = preorder[0]
        rootIndex = 0
        for idx, elem in enumerate(inorder):
            if elem == rootVal:
                rootIdx = idx
                break
        
        left = inorder[:rootIdx]
        right = inorder[rootIdx+1:]
        
        root = TreeNode(rootVal)
        root.left = self.buildTree(preorder[1:1+rootIdx], left)
        root.right = self.buildTree(preorder[1+rootIdx:], right)
        
        return root
        