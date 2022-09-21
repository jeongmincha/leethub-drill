# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        depth = 0
        queue = [root]
        
        while queue:
            current_height_nodes = []
            while queue:
                current_height_nodes.append(queue.pop())
            
            depth += 1
            
            for c in current_height_nodes:
                if c and c.left:
                    queue.append(c.left)
                if c and c.right:
                    queue.append(c.right)
        
        return depth