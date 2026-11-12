class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        else:
            brackets = {")":"(","]":"[","}":"{"}
            stack=[]
            for i in s:
                if i in brackets:
                    top_element= stack.pop() if stack else "#"
                    if brackets[i]!=top_element:
                        return False
                else: 
                    stack.append(i)
            return not stack

