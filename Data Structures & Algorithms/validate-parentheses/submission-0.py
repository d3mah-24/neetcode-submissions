class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hash={"}":"{",")":"(","]":"["}
        for a in s:
            b= hash.get(a)
            if not b:
                stack.append(a) 
            elif not stack or stack[-1]!=b:
                return False 
            else:
                stack.pop()
        return not stack