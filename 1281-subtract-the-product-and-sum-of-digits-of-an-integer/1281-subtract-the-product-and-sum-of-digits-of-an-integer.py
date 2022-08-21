class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l = []
        while n > 0:
            l.insert(0, n % 10)
            n //= 10

        p = 1
        s = 0
        for e in l:
            p *= e
            s += e

        return p-s  