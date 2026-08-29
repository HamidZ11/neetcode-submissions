class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydictionary = {}
        result = []

        for i, num in enumerate(nums):
            need = target - num
            
            if need in mydictionary:
                result.append(mydictionary[need])
                result.append(i)
                return result
                
            
            else:
                mydictionary[num] = i



