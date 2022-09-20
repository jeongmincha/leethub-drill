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
        
        for (i, j), cnt in self.points.items():
            if i == x or j == y or abs(x-i) != abs(y-j):
                continue
            res += cnt * self.points[i, y] * self.points[x, j]

        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)