class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        my_dict = {}
        results = []

        for num in nums:

            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        for i in range(k):
            current_max = max(my_dict, key=my_dict.get)
            results.append(current_max)
            del my_dict[current_max]

        return results


            


        