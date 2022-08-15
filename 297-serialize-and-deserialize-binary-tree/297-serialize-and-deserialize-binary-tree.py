# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        
        def dfs(node):
            if node is None:
                res.append("null")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        l = data.split(",")
        idx = 0
        
        def dfs():
            nonlocal idx
            if l[idx] == "null":
                idx += 1
                return None
            
            root = TreeNode(int(l[idx]))
            idx += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))