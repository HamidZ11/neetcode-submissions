class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.lower()
        left = 0
        right = len(new_s) - 1
        while left < right:
            if not new_s[left].isalnum():
                left += 1
                continue
            if not new_s[right].isalnum():
                right -= 1
                continue
            if new_s[left] != new_s[right]: 
                return False
            else:
                left +=1
                right -=1
        return True