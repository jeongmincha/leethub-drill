class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        target = sorted([int(_) for _ in str(n)])
        for i in range(30):
            if sorted([int(_) for _ in str(1 << i)]) == target:
                return True
        return False