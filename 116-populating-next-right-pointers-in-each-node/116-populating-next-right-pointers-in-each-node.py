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
        current_nodes = [root] # nodes at the the current height
        
        while len(current_nodes) > 0:
            next_nodes = [] # nodes at the next height
            
            for node in current_nodes:
                if node and node.left:
                    next_nodes.append(node.left)
                if node and node.right:
                    next_nodes.append(node.right)
            
            for i in range(len(next_nodes)-1):
                next_nodes[i].next = next_nodes[i+1]
            
            current_nodes = next_nodes
        
        return root