class Solution:
    def isValid(self, s: str) -> bool:
        mystack = []
        matches = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in "({[":
                mystack.append(char)
            else: 
                if not mystack:
                    return False
                else:
                    top = mystack.pop()
                    if top != matches[char]:
                        return False
        
        return not mystack

