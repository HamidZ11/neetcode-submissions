class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = []
        right = []
        product = 1
        results = []


        for i in nums:
            left.append(product)
            product = product * i
        
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            right.append(product)
            product = product * nums[i]
        
        right.reverse()
        
        for i in range(len(nums)):
            results.append(left[i] * right[i])
        
        return results
            


