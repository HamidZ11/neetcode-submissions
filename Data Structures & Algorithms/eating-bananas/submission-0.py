class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left <= right:
            hours_taken = 0
            k = (left + right) // 2
            for i in piles: 
                if i <= k:
                    hours_taken +=1
                else: 
                    if i % k > 0:
                        hours_taken += (i // k) + 1
                    else:
                        hours_taken += i // k 

            if hours_taken <= h:
                answer = k 
                right = k-1
            
            else:
                left = k + 1
        
        return answer


