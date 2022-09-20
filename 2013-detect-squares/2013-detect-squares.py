from collections import Counter

class DetectSquares:

    def __init__(self):
        self.points = Counter()
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[x, y] += 1
        

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point
        
        if len(self.points) < 1000:
            for (i, j), cnt in self.points.items():
                if i == x or j == y or abs(x-i) != abs(y-j):
                    continue
                res += cnt * self.points[i, y] * self.points[x, j]
            return res
        
#         for i in range(0, 1001):
#             if i == x:
#                 continue
            
#             d = abs(x-i)
#             for j in [y+d, y-d]:
#                 res += self.points[i, j] * self.points[x, j] * self.points[i, y]
        
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)