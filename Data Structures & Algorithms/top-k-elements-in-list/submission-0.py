class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}  
        for i in nums:  
            freq_dict[i] = freq_dict.get(i,0) + 1

        bucket = [[] for i in range(len(nums) + 1)]
        for num,count in freq_dict.items(): 
            bucket[count].append(num)

        result = []  
        for i in range(len(bucket) - 1, 0, -1):  
            result.extend(bucket[i]) 
            if len(result) ==k:
                return result
        