class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) -1
        while i < j:
            total = numbers[i] + numbers[j]
            if total == target:
                return [i+1,j+1]
            if total < target:
                i+=1
            elif total > target:
                j-=1
        return None
