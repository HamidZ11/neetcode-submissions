class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        window_freq = {}
        left = 0

        for letter in s1:
            if letter in s1_freq:
                s1_freq[letter] += 1
            else:
                s1_freq[letter] = 1

        for right in range(len(s2)):
            if s2[right] in window_freq:
                window_freq[s2[right]] += 1
            else:
                window_freq[s2[right]] =1

            if right - left + 1 > len(s1):
                window_freq[s2[left]] -= 1

                if window_freq[s2[left]] == 0:
                    del window_freq[s2[left]]

                left += 1

            if window_freq == s1_freq:
                return True

        return False