class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # so i have two arrays and i need to find the numbers that are present in both arrays. 
        # i will convert both arrays into sets

        # that was simple enough but i have to have a way of preventing duplicates, i think sets prevent duplicates

        set1 = set(nums1)
        set2 = set(nums2)
        results = []

        for num in nums1:
            if num in set2:
                if num not in results: 
                    results.append(num)
        for num in nums2:
            if num in set1:
                if num not in results: 
                    results.append(num)

        return results 
                