class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = {}
        for i, j in enumerate(numbers):
            if target-j in x:
                return [x[target-j]+1,i+1]
            x[j] = i