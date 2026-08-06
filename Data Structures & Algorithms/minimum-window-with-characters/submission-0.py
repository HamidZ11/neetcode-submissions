class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = {}
        window_freq = {}
        have = 0
        left = 0
        res = "" 
        res_len = float("inf")

        for letter in t:
            t_freq[letter] = t_freq.get(letter, 0) + 1
        need = len(t_freq)

        for right in range(len(s)):
            window_freq[s[right]] = window_freq.get(s[right], 0) + 1
            if s[right] in t_freq and window_freq[s[right]] == t_freq[s[right]]:
                have += 1
                while have == need:
                    if (right - left + 1) < res_len:
                        res_len = right - left + 1
                        res = s[left:right + 1]

                    window_freq[s[left]] -= 1
                    if s[left] in t_freq and window_freq[s[left]] < t_freq[s[left]]:
                        have -=1
                    left += 1
    
        return res