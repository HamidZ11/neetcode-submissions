class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if the strings are the same length, then we just have to check the 

        
        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False
        
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] +=1

        
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] +=1
        
        if s_dict == t_dict:
            return True
        else:
            return False

        
