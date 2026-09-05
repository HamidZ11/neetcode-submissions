class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        myhashmap = {}
        results = []

        for i,num in enumerate(nums): 
            need = target - num

            if need in myhashmap:
                return [myhashmap[need], i]
            else:
                myhashmap[num] = i
        
        





