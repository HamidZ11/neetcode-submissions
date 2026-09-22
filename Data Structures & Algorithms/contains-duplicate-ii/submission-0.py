class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dup_dict = {}

        for index, num in enumerate(nums):

            if num in dup_dict:
                if abs(dup_dict[num] - index) <= k:
                    return True
            

            dup_dict[num] = index
        
        return False
        