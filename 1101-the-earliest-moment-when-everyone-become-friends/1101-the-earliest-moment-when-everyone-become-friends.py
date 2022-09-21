class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find_parent(self, node):
        parent_node = self.parent[node]
        if parent_node == node:
            return node
        
        self.parent[node] = self.find_parent(parent_node)
        return self.parent[node]
    
    def union(self, x, y):
        parent_x = self.find_parent(x)
        parent_y = self.find_parent(y)
        
        if parent_x != parent_y:
            size_x = self.size[x]
            size_y = self.size[y]
            
            # make sure y is a bigger parent
            if size_x > size_y:
                x, y = y, x
                parent_x, parent_y = parent_y, parent_x
            
            self.parent[parent_x] = parent_y # parent_y will be the parent of parent_x
            self.size[parent_y] += self.size[parent_x]

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs = sorted(logs, key=lambda x: x[0])
        disjoint_set = DisjointSet(n)
        
        for timestamp, x, y, in logs:
            disjoint_set.union(x, y)
            # after union, the parents of x and y are the same.
            parent = disjoint_set.find_parent(x)
            
            if disjoint_set.size[parent] == n:
                return timestamp
        
        return -1