class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array = []
        prefix = 1 
        for i in nums:
            left_array.append(prefix)
            prefix = prefix * i
        
        right_array = []
        right_prefix = 1 
        for i in reversed(nums):
            right_array.append(right_prefix)
            right_prefix = right_prefix * i
        right_array.reverse()
        
        full_array = []
        for i, val in enumerate(left_array):
            full_array.append(val * right_array[i])
        return full_array