class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}

        for i in s:
            if i not in s_dict:
                s_dict[i] = 1
            else:
                s_dict[i] = s_dict[i] + 1

        for i in t:
            if i not in s_dict:
                return False
            else:
                s_dict[i] = s_dict[i] - 1
                if s_dict[i] < 0:
                    return False

        return True