class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n:
            total+= n & 1
            n >>= 1
        return total
