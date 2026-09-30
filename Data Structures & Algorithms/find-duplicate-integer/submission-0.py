class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        new_set = set()

        for num in nums:
            if num in new_set:
                return num
            else: 
                new_set.add(num)
        
        