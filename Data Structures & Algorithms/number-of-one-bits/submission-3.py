class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # 23 = 0001 0111
        # How did i do that in my head? I did the bigget bit that goes into 23 (16) and so on, i went from there

        one_count = 0
        power = 32
        while n != 0:
            if n - pow(2,power) >= 0:
                n = n - pow(2,power)
                one_count += 1
            power -= 1

        return one_count
