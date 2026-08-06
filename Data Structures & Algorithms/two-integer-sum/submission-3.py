class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            current = nums[i]
            need = target - current

            if need in d:
                return [d[need], i]
            else:
                d[current] = i
                

