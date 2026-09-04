class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        myhash = {}

        for index, num in enumerate(nums):
            need = target - num
            if need in myhash:
                return [min(index, myhash[need]), max(index, myhash[need])]
            else: 
                myhash[num] = index










