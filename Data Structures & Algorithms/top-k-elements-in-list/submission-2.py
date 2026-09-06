class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        def get_freq(pair):
            return pair[1]
        
        result = []
        my_dict = {}

        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1
        
        pairs = list(my_dict.items()) # give dictionary as key-value pairs
        # Without .items(), iterating over a dictionary gives you just the keys

        pairs.sort(key=get_freq, reverse=True) 
        # sort pairs, use the get_freq method as your sorting key, and reverse is true meaning its highest first


        for i in range(k):
            result.append(pairs[i][0]) # results list appends the value at inedx pos 0 for i in pairs
        
        return result



        