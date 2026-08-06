class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        tempstack = []
        for index, temp in enumerate(temperatures):
             while tempstack and tempstack[-1][1] < temp:
                prev_index, prev_temp = tempstack.pop()
                results[prev_index] = index - prev_index
        
             tempstack.append((index, temp))

        return results


