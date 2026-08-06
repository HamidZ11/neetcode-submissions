class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_dict = {}
        left = 0 
        max_len= 0 
        for right in range(len(s)): 
            freq_dict[s[right]] = freq_dict.get(s[right], 0) + 1
            window_size = right - left + 1
            max_frequency = max(freq_dict.values())
            if window_size - max_frequency > k:
                freq_dict[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len