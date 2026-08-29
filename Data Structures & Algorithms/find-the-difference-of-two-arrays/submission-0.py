class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        uniq1 = []
        uniq2 = []

        for num in set1:
            if num not in set2:
                uniq1.append(num)
            
        for num in set2:
            if num not in set1:
                uniq2.append(num)
        
        result = [uniq1, uniq2]

        return result