class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            numsum = numbers[left] + numbers[right]
            if numsum > target:
                right -= 1
            if numsum < target:
                left +=1
            if numsum == target:
                return [left + 1, right + 1]