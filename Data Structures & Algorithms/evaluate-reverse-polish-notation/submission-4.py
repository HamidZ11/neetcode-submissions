class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+" , "-", "*", "/"]
        mystack = []
        for i in tokens:
            if i in operators: 
                right = mystack.pop()
                left = mystack.pop()
                if i == "+":
                    result = left + right
                    mystack.append(result)
                elif i == "-":
                    result = left - right
                    mystack.append(result)
                elif i == "*":
                    result = left * right
                    mystack.append(result)
                elif i == "/":
                    result = left / right
                    mystack.append(int(result))
            else:
                mystack.append(int(i))
        
        return mystack[-1]
                
