"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        
        _left = root.left
        _right = root.right
        
        while _left:
            _left.next = _right
            _left = _left.right
            _right = _right.left
        
        self.connect(root.left)
        self.connect(root.right)
        
        return root