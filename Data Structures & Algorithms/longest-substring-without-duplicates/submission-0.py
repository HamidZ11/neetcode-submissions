class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        max_len = 0
        dup_set = set()
        for right in range(len(s)):
            while s[right] in dup_set:
                dup_set.remove(s[left])
                left += 1
            dup_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len

